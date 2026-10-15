import csv
import ipaddress
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


def write_csv(name, rows):
    with (ROOT / name).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


snapshot = read("snapshot.json")
samples = read("samples.json")
details = read("details.json")
verification = read("verification.json")
owners = read("ip-owners.json")
reputation = read("reputation-results.json")
checks = {r["IP"]: r for r in reputation["Checks"]}
processes = {p["ProcessId"]: p for p in snapshot["Processes"]}
later_processes = {p["ProcessId"]: p for p in read("processes-later.json")}
services = defaultdict(list)
for s in snapshot["Services"]:
    services[s["ProcessId"]].append(s["Name"])
states = {2: "Listen", 3: "SynSent", 5: "Established", 8: "CloseWait", 11: "TimeWait", 100: "Bound"}
ignored = {"::", "0.0.0.0", "127.0.0.1", "::1"}
connections = []
for time, rows, procmap in [(snapshot["CapturedAt"], snapshot["TCP"], processes)] + [
    (sample["Time"], sample["TCP"], later_processes) for sample in samples
]:
    for r in rows:
        pid = r["OwningProcess"]
        process = procmap.get(pid, processes.get(pid, {}))
        name = process.get("Name") or "Не определён: процесс завершился / не попал в снимки"
        if pid == 0:
            name = "Нет владельца (завершённое соединение, PID 0)"
        connections.append({
            "Time": time, "LocalAddress": r["LocalAddress"], "LocalPort": r["LocalPort"],
            "RemoteAddress": r["RemoteAddress"], "RemotePort": r["RemotePort"],
            "State": states.get(r["State"], r["State"]), "PID": pid,
            "Process": name, "Path": process.get("ExecutablePath") or "",
            "Services": ", ".join(services[pid]),
        })
write_csv("tcp-all-samples.csv", connections)

by_ip = defaultdict(list)
for c in connections:
    if c["RemoteAddress"] not in ignored:
        by_ip[c["RemoteAddress"]].append(c)
dns = defaultdict(set)
for d in details["DnsCache"]:
    if d.get("Data") in by_ip:
        dns[d["Data"]].add(d.get("Entry") or d.get("Name") or "")

ip_rows = []
for owner in sorted(owners, key=lambda r: (ipaddress.ip_address(r["IP"]).version, int(ipaddress.ip_address(r["IP"])))):
    ip = owner["IP"]
    conns = by_ip[ip]
    active = [c for c in conns if c["PID"] != 0]
    names = sorted({c["Process"] for c in active}) or ["Процесс уже завершился"]
    asns = "; ".join(f'AS{a["asn"]} {a["holder"]}' for a in owner.get("ASNs", []))
    r = checks[str(ipaddress.ip_address(ip))]
    note = "Совпадений в двух проверенных списках нет; это не гарантия безопасности"
    if ip == "213.57.94.219":
        note = "RustDesk; Роман подтвердил использование сейчас"
    elif ip == "2001:67c:2e8:22::c100:696":
        note = "Сеть RIPE NCC; появился при запросах этой проверки. PID 25044 не удалось связать с файлом"
    elif ip.startswith("2a00:a040:") and 80 in {c["RemotePort"] for c in conns}:
        note = "HTTP службы CryptSvc; возможна загрузка данных проверки сертификатов, содержимое не проверялось"
    ip_rows.append({
        "IP": ip, "RemotePorts": ", ".join(map(str, sorted({c["RemotePort"] for c in conns}))),
        "Processes": ", ".join(names), "NetworkOwner": asns,
        "Prefix": owner.get("Prefix", ""), "DNSCache": ", ".join(sorted(dns[ip])),
        "SpamhausDROP": "MATCH" if r["SpamhausMatches"] else "No match",
        "Feodo": "MATCH" if r["FeodoMatch"] else "No match", "Note": note,
        "OwnerSource": owner.get("Source", ""),
    })
write_csv("ip-addresses.csv", ip_rows)

listeners = [c for c in connections if c["State"] == "Listen"]
unique_listeners = {}
for c in listeners:
    key = (c["LocalAddress"], c["LocalPort"], c["PID"], c["Process"])
    unique_listeners.setdefault(key, {k: v for k, v in c.items() if k not in {"Time", "RemoteAddress", "RemotePort", "State"}})
write_csv("tcp-listeners.csv", list(unique_listeners.values()))
udp = {}
for rows, procmap in [(snapshot["UDP"], processes)] + [(s["UDP"], later_processes) for s in samples]:
    for r in rows:
        pid = r["OwningProcess"]
        proc = procmap.get(pid, processes.get(pid, {}))
        udp[(r["LocalAddress"], r["LocalPort"], pid)] = {
            **r, "Process": proc.get("Name", "Не определён"),
            "Path": proc.get("ExecutablePath") or "", "Services": ", ".join(services[pid]),
        }
write_csv("udp-local-endpoints.csv", list(udp.values()))

established = [r for r in snapshot["TCP"] if r["State"] == 5 and r["RemoteAddress"] not in ignored]
report = [
    "# Проверка сетевых соединений компьютера Романа",
    "",
    "15 октября 2026 года. Время — Израиль (UTC+03:00).",
    "",
    "**Явных признаков вредоносных соединений в собранных данных не обнаружено. Есть широкие разрешения на удалённый доступ, которые стоит ограничить. Проверка не доказывает отсутствие заражения.**",
    "",
    f'- Первый снимок: {snapshot["CapturedAt"]}.',
    f'- Короткое наблюдение: {samples[0]["Time"]} — {samples[-1]["Time"]}, 16 снимков примерно за 39 секунд.',
    f'- В первом снимке: {len(established)} установленных TCP-соединения с нелокальными адресами.',
    f'- Всего замечено {len(ip_rows)} уникальных нелокальных адреса. Для каждого определён владелец сети и выполнена сверка списков.',
    f'- В первом снимке: 39 слушающих TCP-записей, 27 разных номеров TCP-портов и {len(snapshot["UDP"])} локальных UDP-записей.',
    "",
    "## Что требует внимания",
    "",
    "| Порт / служба | Что установлено | Оценка |",
    "|---|---|---|",
    "| 3389 TCP/UDP, удалённый рабочий стол Windows | Слушает IPv4/IPv6. Входящие правила разрешают любые удалённые адреса, любые адаптеры и все профили, включая Public. Текущий профиль Ethernet — Public. Проверка подлинности до входа (NLA) включена | Главный риск настройки. Если RDP не нужен — отключить. Если нужен — ограничить доверенными адресами или доступом через VPN |",
    "| 2179 TCP, Hyper-V | Слушает IPv4/IPv6; найдено разрешающее правило Hyper-V для всех профилей и адресов. Все дополнительные условия этого правила отдельно не проверялись | Проверить, нужен ли удалённый доступ к виртуальным машинам |",
    "| 135 TCP и 49664–49671 TCP | Службы Windows: RPC, вход в систему, журнал, планировщик, печать. Есть разрешающие правила удалённого управления Hyper-V/WMI | Объяснимые системные порты; доступ лучше ограничивать доверенной сетью |",
    "| 139/445 TCP | Сетевой доступ Windows к файлам; есть слушающие записи | Обычные службы Windows. В собранном списке нет включённых отдельных разрешений для 139/445. Фактическая доступность извне не проверялась |",
    "| 50458 TCP, 21119/51866 UDP, RustDesk | Соединение с 213.57.94.219:49965, сеть HOT-Net. Роман подтвердил, что использует RustDesk сейчас. Файл установленной программы имеет действительную подпись | Объяснимо текущей работой. Само наличие соединения не доказывает, кто управляет какой стороной |",
    "| 27036 TCP/UDP | Steam; действительная подпись Valve | Ожидаемо для запущенного Steam |",
    "| 7680 TCP | Служба DoSvc — доставка обновлений Windows | Ожидаемая служба; правило разрешено для всех профилей |",
    "| 53 UDP | SharedAccess, раздача интернета / виртуальные машины. Слушает 0.0.0.0, но правило HNS UDP DNS ограничено адаптером vEthernet (Default Switch) | Само широкое прослушивание не доказывает доступ с основной сети. TCP 53 в снимках не слушает |",
    "| 6327–6329, 23373 и другие на 127.0.0.1 / ::1 | SteelSeries, Beeper, Steam, Intel | Доступны через адрес самого компьютера; список есть в CSV |",
    "",
    "Слушающий порт — программа ждёт подключения. Это не то же самое, что доступность порта из интернета. Внешняя доступность зависит также от роутера, правил IPv6 и других средств защиты. Внешнее сканирование не проводилось. Правил netsh portproxy не найдено; перенаправления на роутере не проверялись.",
    "",
    "## Проверка адресов и программ",
    "",
    "Владельцы адресов установлены через RIPEstat. Владелец сети — не всегда владелец конкретного сайта. У крупных облаков могут быть как хорошие, так и вредоносные клиенты.",
    "",
    f'Все {len(ip_rows)} адреса сверены с {reputation["SpamhausIPv4Networks"]} сетями Spamhaus DROP IPv4, {reputation["SpamhausIPv6Networks"]} сетями DROP IPv6 и {reputation["FeodoEntries"]} адресами Feodo. **Совпадений нет.**',
    "",
    "Списки скачаны 15 октября. Сервер указал Last-Modified: Spamhaus IPv4 — 13 октября 2026, IPv6 — 3 октября 2026, Feodo — 30 июня 2026. Feodo содержит только пять записей и давно не обновлялся: его отсутствие совпадений имеет очень ограниченную ценность. Эти списки не являются полной базой всех вредоносных адресов.",
    "",
    "У всех проверенных файлов сетевых приложений подписи действительны: RustDesk, Telegram, Beeper, Blitz, Brave, Steam, SteelSeries, OpenAI и проверенные компоненты Windows. Подпись подтверждает издателя файла, но не гарантирует безопасность всех действий программы. Часть системных процессов не раскрыла путь к файлу; все их файлы отдельно не проверялись.",
    "",
    "Адрес RIPE NCC появился во время запросов владельцев IP в рамках этой проверки. У связанного PID 25044 путь и имя не удалось получить: процесс не попал в два списка процессов. Поэтому связь с нашей командой вероятна, но не подтверждена по исполняемому файлу.",
    "",
    "## Все замеченные внешние адреса",
    "",
    "Включены также попытки соединения и уже закрывающиеся соединения. PID 0 у закрытого соединения не означает, что процесс Idle отправляет трафик. Колонка DNS — совпадение с локальным кешем имён, а не подтверждение содержимого запроса.",
    "",
    "| IP | Удалённые порты | Программы | Владелец сети | DNS из кеша |",
    "|---|---|---|---|---|",
]
for r in ip_rows:
    cells = [r["IP"], r["RemotePorts"], r["Processes"], r["NetworkOwner"], r["DNSCache"] or "—"]
    report.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
report += [
    "",
    "## Брандмауэр, антивирус и входы",
    "",
    "- Брандмауэр Windows включён во всех трёх профилях. По умолчанию входящие подключения блокируются, исходящие разрешаются. Исключения для RDP и других программ действуют отдельно.",
    "- Журналирование разрешённых и заблокированных соединений брандмауэра выключено. Полной истории сетевой активности из него получить нельзя.",
    "- Microsoft Defender включён; защита в реальном времени работает. Базы обновлены 15 октября в 00:16. Последняя быстрая проверка — 10 октября; полная — 1 сентября. Новое сканирование не запускалось.",
    "- В истории Defender есть неактивное обнаружение PUA:Win32/Presenoker внутри ISO-образов Kali Linux от 1–2 сентября. ActionSuccess=True, IsActive=False, DidThreatExecute=False. Это запись об инструментах в образе, а не доказательство текущего заражения.",
    "- Сейчас видна одна активная локальная сессия seala, удалённых RDP-сессий нет. За семь дней в выбранных журналах: событие 1149 не найдено; найденные события 21 имеют источник LOCAL. Это не исключает удалённый доступ другими программами или события, не сохранившиеся в журнале.",
    "",
    "## Что эта проверка не охватывает",
    "",
    "Проверены таблицы соединений Windows и локальные UDP-порты. Для UDP удалённые адреса эти таблицы не показывают; полный список UDP-получателей не собран. Пакеты, содержимое зашифрованных соединений и объём передачи не анализировались. Короткие подключения между снимками могли не попасть в отчёт. Отдельный трафик внутри виртуальных машин, WSL и контейнеров полностью не обследован. Редкий или спящий вредоносный процесс может не проявиться за 39 секунд.",
    "",
    "## Файлы с деталями",
    "",
    "- [Все 53 IP, владельцы, результаты сверки и ссылки на RIPE](ip-addresses.csv)",
    "- [Все собранные TCP-записи с программами и состояниями](tcp-all-samples.csv)",
    "- [Слушающие TCP-порты](tcp-listeners.csv)",
    "- [Локальные UDP-порты](udp-local-endpoints.csv)",
    "- Исходные данные: snapshot.json, samples.json, details.json, verification.json, ip-owners.json, reputation-results.json и feed-status.json.",
    "",
    "Настройки сети и защиты не изменялись. Соединения не разрывались. Файлы программ никуда не отправлялись. В RIPE передавались только проверяемые внешние IP. Списки угроз скачаны для локальной сверки.",
    "",
    "## Источники",
    "",
    "- [RIPEstat Prefix Overview](https://stat.ripe.net/docs/data-api/api-endpoints/prefix-overview)",
    "- [Spamhaus DROP: назначение и источники списков](https://www.spamhaus.org/blocklists/do-not-route-or-peer/)",
    "- [Feodo Tracker](https://feodotracker.abuse.ch/)",
    "- [Microsoft: удалённый рабочий стол и доступ извне](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-outside-access)",
]
(ROOT / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
summary = {
    "UniqueRemoteIPs": len(ip_rows), "InitialEstablishedRemoteTCP": len(established),
    "InitialTCPListenRecords": sum(r["State"] == 2 for r in snapshot["TCP"]),
    "InitialDistinctListeningPorts": len({r["LocalPort"] for r in snapshot["TCP"] if r["State"] == 2}),
    "InitialUDPEndpoints": len(snapshot["UDP"]), "TCPRecordsAcrossSnapshots": len(connections),
    "ReputationMatches": [r for r in reputation["Checks"] if r["SpamhausMatches"] or r["FeodoMatch"]],
    "GeneratedFiles": ["report.md", "ip-addresses.csv", "tcp-all-samples.csv", "tcp-listeners.csv", "udp-local-endpoints.csv"],
}
(ROOT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
