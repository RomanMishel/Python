import requests
import json

url = "https://api.livecoinwatch.com/coins/single"

payload = json.dumps({
  "currency": "USD",
  "code": "TONCOIN",
  "meta": True
})
headers = {
  'content-type': 'application/json',
  'x-api-key': 'c2ea5b77-1668-46f1-9089-e1691c6ff332'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_json= response.json()
price = response_json['rate']
print(price)