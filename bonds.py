import requests

send_req = requests.get("https://www.livecoinwatch.com/price/Toncoin-TONCOIN")

print(send_req.text)