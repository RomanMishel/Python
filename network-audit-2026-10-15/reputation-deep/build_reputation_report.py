import csv
import ipaddress
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIT = ROOT.parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


original = list(csv.DictReader((AUDIT / "ip-addresses.csv").open(encoding="utf-8-sig", newline="")))
otx_rows = read("otx-summary.json")
otx = {r["IP"]: r for r in otx_rows}
phish_queries = read("phishstats-summary.json")
phish = {ip: q for q in phish_queries for ip in q["IPs"]}
feeds = read("extra-feeds-results.json")
assert len(original) == len(otx) == len(phish) == 53
assert {r["IP"] for r in original} == set(otx) == set(phish)
assert all(r["Status"] == "OK" for r in otx_rows + phish_queries)
assert all(q["Count"] == 0 for q in phish_queries)
control_latest = read("phishstats-control-latest.json")
control_filter = read("phishstats-control-filter.json")
assert control_latest and control_filter

specific = {
    "34.95.69.49": "Требует уточнения: исторические жалобы AbuseIPDB; 9 сообщений OTX. Программа в утреннем снимке не определена",
    "13.224.245.88": "6 сообщений OTX; Amazon CloudFront, соединение Brave. Фишинг именно посещённого сайта не подтверждён",
    "149.154.167.41": "30 сообщений OTX; сеть Telegram, подключение Beeper. Упоминания сервиса в атаках не доказывают вредоносность этой сессии",
    "149.154.167.91": "50 сообщений в ответе OTX; сеть Telegram, подключение Beeper. Есть дубли и общие подборки",
    "149.154.167.92": "40 сообщений OTX; сеть Telegram, подключение Telegram.exe. Есть дубли и общие подборки",
}
csv_rows = []
for r in original:
    ip = r["IP"]
    pulse = otx[ip]
    matches = [name for name, result in feeds.items() if result["Matches"].get(ip)]
    csv_rows.append({
        "IP": ip, "ProgramsInSnapshot": r["Processes"], "NetworkOwner": r["NetworkOwner"],
        "OTXPulsesReturnedCount": pulse["PulseCount"], "PhishStatsQueryRecords": phish[ip]["Count"],
        "BlocklistDE": "MATCH" if feeds["blocklist-de"]["Matches"].get(ip) else "No match",
        "CINS": ("Not covered: IPv6" if ":" in ip else "MATCH" if feeds["cins"]["Matches"].get(ip) else "No match"),
        "EmergingThreats": ("Not covered: IPv6" if ":" in ip else "MATCH" if feeds["emergingthreats"]["Matches"].get(ip) else "No match"),
        "Assessment": specific.get(ip, "В проверенных источниках сообщений и совпадений не найдено; безопасность не гарантируется"),
        "OTXSource": pulse["Source"], "OTXFetchedAt": pulse["FetchedAt"],
        "PhishStatsSource": phish[ip]["Source"], "PhishStatsFetchedAt": phish[ip]["FetchedAt"],
    })
with (AUDIT / "ip-reputation-deep.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(csv_rows[0]))
    writer.writeheader()
    writer.writerows(csv_rows)

evidence = {
    "AbuseIPDBHistoricalCopy": {
        "IP": "34.95.69.49", "Source": "https://www.abuseipdb.com/check/34.95.69.49",
        "Reports": 25, "DistinctSources": 7, "DisplayedConfidenceOfAbuse": 8,
        "LatestVisibleAbsoluteTimestampUTC": "2026-03-31T13:27:10Z",
        "Categories": ["Port Scan", "Hacking", "Brute-Force", "SSH"],
        "Caveat": "Read through indexed web copy. Direct request returned HTTP 403. Current live count/score not confirmed. Relative dates in the copy are stale; use absolute dates. Score is not infection probability.",
    },
    "PublicContext": [
        {"IP": "131.153.232.252", "Source": "https://urlscan.io/ip/131.153.232.252", "Observation": "Historic observed aditude.cloud hostnames; not a phishing verdict and not proof of the local connection hostname"},
        {"IP": "169.150.202.210", "Source": "https://urlscan.io/result/0197cf62-6a41-76ef-be2e-26c9b24529f9/", "Observation": "Historic scan of edgezone-isr.bunnyinfra.net, no classification; not a current clean verdict"},
        {"IP": "34.95.69.49", "Source": "https://urlscan.io/ip/34.95.69.49", "Observation": "Shared infrastructure context; the local connection's hostname and program remain unknown"},
    ],
}
(ROOT / "additional-web-evidence.json").write_text(json.dumps(evidence, indent=2, ensure_ascii=False), encoding="utf-8")

lines = [
    "# Углублённая проверка репутации 53 IP-адресов",
    "",
    "Проверка выполнена 15 октября 2026 года примерно в 11:47–11:53 по времени Израиля (UTC+03:00). Проверены адреса из утреннего снимка соединений около 09:21–09:24. Новый полный снимок текущих соединений не собирался.",
    "",
    "**Есть адреса с историческими жалобами и сообщениями об угрозах. Подтверждённую связь соединений Романа с фишинговой кампанией установить не удалось. Главный адрес для уточнения — 34.95.69.49.**",
    "",
    "## Что проверено",
    "",
    "- AlienVault OTX: отдельный успешный запрос для каждого из 53 IP, включая 37 IPv6. Для 48 адресов ответ не содержит сообщений (pulses), для пяти содержит. Значение reputation=0 не трактуется как сертификат безопасности.",
    "- PhishStats: 16 отдельных запросов IPv4 и четыре групповых запроса IPv6. Все 53 адреса охвачены; ответы пустые. Работоспособность сервиса и фильтра OR проверена на контрольной свежей записи, которая успешно вернулась.",
    f'- blocklist.de: сверка со списком {feeds["blocklist-de"]["Entries"]} адресов, включая {feeds["blocklist-de"]["IPv6Entries"]} IPv6. Совпадений нет.',
    f'- CINS Army: сверка 16 IPv4 с {feeds["cins"]["Entries"]} записями. Совпадений нет. Загруженный список не содержит IPv6.',
    f'- Emerging Threats compromised-ips: сверка 16 IPv4 с {feeds["emergingthreats"]["Entries"]} записями. Совпадений нет. Загруженный список не содержит IPv6.',
    "- Дополнительно изучены доступные публикации по пяти адресам с сообщениями OTX и контекст сетей. AbuseIPDB изучен выборочно; полной проверки всех 53 IP в AbuseIPDB и VirusTotal не было.",
    "",
    "## Пять адресов с упоминаниями",
    "",
    "| Адрес | Что найдено | Что это значит для Романа |",
    "|---|---|---|",
    "| **34.95.69.49** | Google Cloud. 9 сообщений OTX; есть общие подборки, сообщения о сканировании и отслеживании. В доступной копии AbuseIPDB: 25 жалоб от 7 источников, показатель 8; категории — сканирование портов, перебор паролей и SSH. Последняя видимая абсолютная дата — 31 марта 2026 | Самый полезный кандидат для уточнения домена и программы. В утреннем снимке только уже завершённое соединение, PID 0. Его нельзя приписать конкретной программе. Содержимое обмена и фишинг не подтверждены |",
    "| **13.224.245.88** | 6 сообщений OTX с названиями об Ebury, в основном похожие и повторяющиеся подборки. OTX отмечает CloudFront/AWS | Соединение открыл Brave. Это общий сервер доставки сайтов; технического подтверждения, что именно посещённый сайт участвовал в кампании, не найдено. Само название пользовательской подборки не доказывает участие адреса в Ebury |",
    "| **149.154.167.41** | 30 сообщений OTX. Сеть Telegram; встречаются подборки об атаках и копии сообщений со ссылкой на CISA об Ivanti | Соединение открыл Beeper. Первичный текст CISA получить не удалось; нельзя считать содержание копий независимо подтверждённым. Доступ к Telegram из Beeper объясним; злоумышленники тоже могут использовать сервис |",
    "| **149.154.167.91** | В ответе OTX 50 сообщений: многочисленные клоны, подборки, сканирования. Сеть Telegram | Соединение открыл Beeper. Это не 50 доказанных независимых кампаний и не доказательство заражения |",
    "| **149.154.167.92** | 40 сообщений OTX, включая пользовательские списки и данные ловушек для атакующих. Есть повторные записи. Сеть Telegram | Соединение открыл подписанный Telegram.exe. В собранных локальных данных нет подтверждения использования чужого бота или утечки |",
    "",
    "Карточка AbuseIPDB доступна через поисковую копию, а прямой запрос вернул HTTP 403. Поэтому 25 жалоб и показатель 8 — значения из доступной копии, а не подтверждённые текущие значения. Показатель 8 не означает 8% вероятности заражения. Относительные даты на странице устарели; в оценке использована абсолютная дата. Некоторые жалобы содержат ответы с исходного порта 443 на высокий порт клиента; такая запись сама по себе ещё не доказывает сканирование.",
    "",
    "## Полная таблица",
    "",
    "Число OTX — сообщения в ответе API. Это пользовательские публикации, среди которых бывают дубли, ошибки и списки обычных сервисов, замеченных рядом с вредоносным образцом. Ноль означает отсутствие найденных сообщений, а не доказанную безопасность. PhishStats для всех строк вернул ноль записей.",
    "",
    "| IP | Программы в утреннем снимке | OTX | Оценка |",
    "|---|---|---:|---|",
]
for r in csv_rows:
    lines.append("| " + " | ".join(str(x).replace("|", "/") for x in [r["IP"], r["ProgramsInSnapshot"], r["OTXPulsesReturnedCount"], r["Assessment"]]) + " |")

lines += [
    "",
    "## Ограничения и следующий полезный шаг",
    "",
    "Фишинг обычно связан с конкретным доменом и страницей. Один IP может обслуживать множество сайтов; хостинг может сменить клиента. Нельзя переносить все исторические жалобы на каждое соединение с этим IP. Для IPv6 охват репутационных баз часто уже; два загруженных дополнительных списка содержат только IPv4.",
    "",
    "Для 34.95.69.49 полезно установить домен и программу, если соединение повторится. Исходный снимок этого не сохранил. Автоматическая блокировка всей сети Google, Amazon или Telegram по этим данным не обоснована. Ни одного файла или пароля эти проверки не анализировали и никуда не отправляли.",
    "",
    "Не проводилась полная проверка VirusTotal, AbuseIPDB или URLhaus: доступ к ним требует дополнительных условий либо был недоступен. Для URLhaus официальный API требует Auth-Key. Это явно ограничивает выводы, и отчёт не представляет собой полную проверку всех баз интернета.",
    "",
    "## Источники и сохранённые ответы",
    "",
    "- [Таблица всех 53 IP с источниками и временем запросов](ip-reputation-deep.csv)",
    "- [OTX API](https://otx.alienvault.com/api/); исходные ответы сохранены в reputation-deep/otx/.",
    "- [PhishStats API и ограничения](https://phishstats.info/api-docs); ответы и контрольные запросы — reputation-deep/phishstats/ и reputation-deep/phishstats-control-*.json.",
    "- [AbuseIPDB: историческая карточка 34.95.69.49](https://www.abuseipdb.com/check/34.95.69.49)",
    "- [blocklist.de: список атакующих за 48 часов](https://www.blocklist.de/en/export.html)",
    "- [CINS Army: назначение списка](https://cinsscore.com/)",
    "- [Emerging Threats: compromised-ips](https://rules.emergingthreats.net/blockrules/compromised-ips.txt)",
    "- [URLhaus: API требует ключ](https://urlhaus.abuse.ch/api/)",
    "",
    "Состояние выгрузок: blocklist.de Last-Modified 15 октября 08:30 UTC; CINS — 15 октября 08:04 UTC; Emerging Threats — 14 октября 21:07 UTC. Метаданные сохранены в reputation-deep/extra-feeds-status.json.",
]
(AUDIT / "reputation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
summary = {
    "IPsChecked": len(csv_rows), "OTXWithPulses": [r["IP"] for r in csv_rows if r["OTXPulsesReturnedCount"]],
    "PhishStatsIPsCovered": len(phish), "PhishStatsRecords": sum(q["Count"] for q in phish_queries),
    "ExtraFeedMatches": {name: {ip: hits for ip, hits in f["Matches"].items() if hits} for name, f in feeds.items()},
    "PrioritizeForAttribution": "34.95.69.49",
    "Files": ["reputation-report.md", "ip-reputation-deep.csv"],
}
(ROOT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
