# Проверка сетевых соединений компьютера Романа

15 октября 2026 года. Время — Израиль (UTC+03:00).

**Явных признаков вредоносных соединений в собранных данных не обнаружено. Есть широкие разрешения на удалённый доступ, которые стоит ограничить. Проверка не доказывает отсутствие заражения.**

- Первый снимок: 2026-10-15T09:21:25.7830552+03:00.
- Короткое наблюдение: 2026-10-15T09:23:11.0429322+03:00 — 2026-10-15T09:23:49.5784631+03:00, 16 снимков примерно за 39 секунд.
- В первом снимке: 82 установленных TCP-соединения с нелокальными адресами.
- Всего замечено 53 уникальных нелокальных адреса. Для каждого определён владелец сети и выполнена сверка списков.
- В первом снимке: 39 слушающих TCP-записей, 27 разных номеров TCP-портов и 59 локальных UDP-записей.

## Что требует внимания

| Порт / служба | Что установлено | Оценка |
|---|---|---|
| 3389 TCP/UDP, удалённый рабочий стол Windows | Слушает IPv4/IPv6. Входящие правила разрешают любые удалённые адреса, любые адаптеры и все профили, включая Public. Текущий профиль Ethernet — Public. Проверка подлинности до входа (NLA) включена | Главный риск настройки. Если RDP не нужен — отключить. Если нужен — ограничить доверенными адресами или доступом через VPN |
| 2179 TCP, Hyper-V | Слушает IPv4/IPv6; найдено разрешающее правило Hyper-V для всех профилей и адресов. Все дополнительные условия этого правила отдельно не проверялись | Проверить, нужен ли удалённый доступ к виртуальным машинам |
| 135 TCP и 49664–49671 TCP | Службы Windows: RPC, вход в систему, журнал, планировщик, печать. Есть разрешающие правила удалённого управления Hyper-V/WMI | Объяснимые системные порты; доступ лучше ограничивать доверенной сетью |
| 139/445 TCP | Сетевой доступ Windows к файлам; есть слушающие записи | Обычные службы Windows. В собранном списке нет включённых отдельных разрешений для 139/445. Фактическая доступность извне не проверялась |
| 50458 TCP, 21119/51866 UDP, RustDesk | Соединение с 213.57.94.219:49965, сеть HOT-Net. Роман подтвердил, что использует RustDesk сейчас. Файл установленной программы имеет действительную подпись | Объяснимо текущей работой. Само наличие соединения не доказывает, кто управляет какой стороной |
| 27036 TCP/UDP | Steam; действительная подпись Valve | Ожидаемо для запущенного Steam |
| 7680 TCP | Служба DoSvc — доставка обновлений Windows | Ожидаемая служба; правило разрешено для всех профилей |
| 53 UDP | SharedAccess, раздача интернета / виртуальные машины. Слушает 0.0.0.0, но правило HNS UDP DNS ограничено адаптером vEthernet (Default Switch) | Само широкое прослушивание не доказывает доступ с основной сети. TCP 53 в снимках не слушает |
| 6327–6329, 23373 и другие на 127.0.0.1 / ::1 | SteelSeries, Beeper, Steam, Intel | Доступны через адрес самого компьютера; список есть в CSV |

Слушающий порт — программа ждёт подключения. Это не то же самое, что доступность порта из интернета. Внешняя доступность зависит также от роутера, правил IPv6 и других средств защиты. Внешнее сканирование не проводилось. Правил netsh portproxy не найдено; перенаправления на роутере не проверялись.

## Проверка адресов и программ

Владельцы адресов установлены через RIPEstat. Владелец сети — не всегда владелец конкретного сайта. У крупных облаков могут быть как хорошие, так и вредоносные клиенты.

Все 53 адреса сверены с 1682 сетями Spamhaus DROP IPv4, 91 сетями DROP IPv6 и 5 адресами Feodo. **Совпадений нет.**

Списки скачаны 15 октября. Сервер указал Last-Modified: Spamhaus IPv4 — 13 октября 2026, IPv6 — 3 октября 2026, Feodo — 30 июня 2026. Feodo содержит только пять записей и давно не обновлялся: его отсутствие совпадений имеет очень ограниченную ценность. Эти списки не являются полной базой всех вредоносных адресов.

У всех проверенных файлов сетевых приложений подписи действительны: RustDesk, Telegram, Beeper, Blitz, Brave, Steam, SteelSeries, OpenAI и проверенные компоненты Windows. Подпись подтверждает издателя файла, но не гарантирует безопасность всех действий программы. Часть системных процессов не раскрыла путь к файлу; все их файлы отдельно не проверялись.

Адрес RIPE NCC появился во время запросов владельцев IP в рамках этой проверки. У связанного PID 25044 путь и имя не удалось получить: процесс не попал в два списка процессов. Поэтому связь с нашей командой вероятна, но не подтверждена по исполняемому файлу.

## Все замеченные внешние адреса

Включены также попытки соединения и уже закрывающиеся соединения. PID 0 у закрытого соединения не означает, что процесс Idle отправляет трафик. Колонка DNS — совпадение с локальным кешем имён, а не подтверждение содержимого запроса.

| IP | Удалённые порты | Программы | Владелец сети | DNS из кеша |
|---|---|---|---|---|
| 13.224.245.88 | 443 | brave.exe | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 13.229.47.174 | 443 | Blitz.exe | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 32.184.75.39 | 443 | brave.exe | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 34.95.69.49 | 443 | Процесс уже завершился | AS396982 GOOGLE-CLOUD-PLATFORM - Google LLC | — |
| 44.241.83.144 | 443 | brave.exe | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 49.13.42.238 | 443 | Beeper.exe | AS24940 HETZNER-AS Hetzner Online GmbH | matrix.beeper.com |
| 57.144.62.145 | 443 | Beeper.exe | AS32934 FACEBOOK - Facebook, Inc. | — |
| 131.153.232.252 | 443 | Blitz.exe | AS19437 SS-ASH - SECURED SERVERS LLC | — |
| 146.75.122.214 | 443 | brave.exe | AS54113 FASTLY - Fastly, Inc. | — |
| 149.154.167.41 | 443 | Beeper.exe | AS62041 Telegram Telegram Messenger Inc | — |
| 149.154.167.91 | 443 | Beeper.exe | AS62041 Telegram Telegram Messenger Inc | — |
| 149.154.167.92 | 443 | Telegram.exe | AS62041 Telegram Telegram Messenger Inc | — |
| 155.133.229.4 | 443 | steam.exe | AS32590 VALVE-CORPORATION - Valve Corporation | cmp1-fra2.steamserver.net |
| 167.233.8.106 | 443 | Процесс уже завершился | AS24940 HETZNER-AS Hetzner Online GmbH | rudderstack.beeper-tools.com |
| 169.150.202.210 | 443 | Blitz.exe | AS60068 CDN77 Datacamp Limited | — |
| 213.57.94.219 | 49965 | rustdesk.exe | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2001:67c:2e8:22::c100:696 | 443 | Не определён: процесс завершился / не попал в снимки | AS3333 RIPE-NCC-AS Reseaux IP Europeens Network Coordination Centre (RIPE NCC) | stat.ripe.net |
| 2400:52e0:1e03::1486:1 | 443 | Blitz.exe | AS200325 BunnyCDN BUNNYWAY, informacijske storitve d.o.o. | — |
| 2600:1901:0:5e8a:: | 443 | Beeper.exe | AS396982 GOOGLE-CLOUD-PLATFORM - Google LLC | o248881.ingest.us.sentry.io |
| 2600:1901:0:85c5:: | 443 | Blitz.exe | AS396982 GOOGLE-CLOUD-PLATFORM - Google LLC | — |
| 2600:9000:21b3:5a00:19:b6f1:d180:93a1 | 443 | Процесс уже завершился | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 2600:9000:2837:7400:1b:cadc:ef40:93a1 | 443 | Blitz.exe | AS16509 AMAZON-02 - Amazon.com, Inc. | — |
| 2603:1020:805:3::402 | 443 | svchost.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2603:1046:c12:c00::2 | 443 | explorer.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2603:1046:c12:1400::2 | 443 | explorer.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2603:1063:2001:3200::365:ff1 | 443 | explorer.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2603:1063:2001:3201::365:ff1 | 443 | explorer.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2603:1063:2001:3203::365:ff1 | 443 | StartMenuExperienceHost.exe | AS8075 MICROSOFT-CORP-MSN-AS-BLOCK - Microsoft Corporation | — |
| 2606:4700::6812:e1d | 443 | Blitz.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700::6812:f1d | 443 | Blitz.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:10::6814:1b19 | 443 | Blitz.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:10::ac42:a08b | 443 | Blitz.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:20::ac43:4969 | 443 | brave.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:3030::ac43:a869 | 443 | brave.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:4403::ac40:94eb | 443 | ChatGPT.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:4409::ac40:961c | 443 | ChatGPT.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2606:4700:440b::6812:2715 | 443 | ChatGPT.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | — |
| 2607:5300:60:4fc1:: | 443 | brave.exe | AS16276 OVH OVH SAS | — |
| 2a00:1450:4001:c21::bc | 5228 | ChatGPT.exe | AS15169 GOOGLE - Google LLC | — |
| 2a00:1450:400c:c0a::bc | 5228 | ChatGPT.exe | AS15169 GOOGLE - Google LLC | — |
| 2a00:1450:4028:806::2003 | 80 | svchost.exe | AS15169 GOOGLE - Google LLC | c.pki.goog |
| 2a00:a040:0:6::4d89:b21b | 80 | svchost.exe | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2a00:a040:0:6::4d89:b23b | 80 | svchost.exe | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2a00:a040:0:186::21cc | 80 | svchost.exe | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2a00:a040:0:197::21cc | 80 | svchost.exe | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2a00:a040:3:2::162 | 53 | Процесс уже завершился | AS12849 HOTNET-IL Hot-Net internet services Ltd. | — |
| 2a01:4f8:1c1d:1014::1 | 443 | Beeper.exe | AS24940 HETZNER-AS Hetzner Online GmbH | matrix.beeper.com |
| 2a01:4f8:c01e:413::1 | 443 | Процесс уже завершился | AS24940 HETZNER-AS Hetzner Online GmbH | matrix.beeper.com |
| 2a03:2880:f319:91:face:b00c:0:6206 | 443 | Beeper.exe | AS32934 FACEBOOK - Facebook, Inc. | — |
| 2a03:2880:f319:120:face:b00c:0:167 | 443, 5222 | Beeper.exe, brave.exe | AS32934 FACEBOOK - Facebook, Inc. | — |
| 2a03:2880:f319:186:face:b00c:0:1cc9 | 443 | Beeper.exe | AS32934 FACEBOOK - Facebook, Inc. | — |
| 2a04:4e42:8e::300 | 443 | Blitz.exe | AS54113 FASTLY - Fastly, Inc. | — |
| 2a06:98c1:3101::6812:202f | 443 | ChatGPT.exe, brave.exe, codex.exe | AS13335 CLOUDFLARENET - Cloudflare, Inc. | chatgpt.com |

## Брандмауэр, антивирус и входы

- Брандмауэр Windows включён во всех трёх профилях. По умолчанию входящие подключения блокируются, исходящие разрешаются. Исключения для RDP и других программ действуют отдельно.
- Журналирование разрешённых и заблокированных соединений брандмауэра выключено. Полной истории сетевой активности из него получить нельзя.
- Microsoft Defender включён; защита в реальном времени работает. Базы обновлены 15 октября в 00:16. Последняя быстрая проверка — 10 октября; полная — 1 сентября. Новое сканирование не запускалось.
- В истории Defender есть неактивное обнаружение PUA:Win32/Presenoker внутри ISO-образов Kali Linux от 1–2 сентября. ActionSuccess=True, IsActive=False, DidThreatExecute=False. Это запись об инструментах в образе, а не доказательство текущего заражения.
- Сейчас видна одна активная локальная сессия seala, удалённых RDP-сессий нет. За семь дней в выбранных журналах: событие 1149 не найдено; найденные события 21 имеют источник LOCAL. Это не исключает удалённый доступ другими программами или события, не сохранившиеся в журнале.

## Что эта проверка не охватывает

Проверены таблицы соединений Windows и локальные UDP-порты. Для UDP удалённые адреса эти таблицы не показывают; полный список UDP-получателей не собран. Пакеты, содержимое зашифрованных соединений и объём передачи не анализировались. Короткие подключения между снимками могли не попасть в отчёт. Отдельный трафик внутри виртуальных машин, WSL и контейнеров полностью не обследован. Редкий или спящий вредоносный процесс может не проявиться за 39 секунд.

## Файлы с деталями

- [Все 53 IP, владельцы, результаты сверки и ссылки на RIPE](ip-addresses.csv)
- [Все собранные TCP-записи с программами и состояниями](tcp-all-samples.csv)
- [Слушающие TCP-порты](tcp-listeners.csv)
- [Локальные UDP-порты](udp-local-endpoints.csv)
- Исходные данные: snapshot.json, samples.json, details.json, verification.json, ip-owners.json, reputation-results.json и feed-status.json.

Настройки сети и защиты не изменялись. Соединения не разрывались. Файлы программ никуда не отправлялись. В RIPE передавались только проверяемые внешние IP. Списки угроз скачаны для локальной сверки.

## Источники

- [RIPEstat Prefix Overview](https://stat.ripe.net/docs/data-api/api-endpoints/prefix-overview)
- [Spamhaus DROP: назначение и источники списков](https://www.spamhaus.org/blocklists/do-not-route-or-peer/)
- [Feodo Tracker](https://feodotracker.abuse.ch/)
- [Microsoft: удалённый рабочий стол и доступ извне](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-outside-access)
