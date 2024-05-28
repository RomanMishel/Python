import requests
import json

currency = input(f'You currency name:'"")
def crypto_currency_request():
    url = "https://api.livecoinwatch.com/coins/single"
    payload = {
    "currency": "USD",
    "code": currency,
    "meta": False
    }
    headers = {
    # 'content-type': 'application/json',
    'x-api-key': 'c2ea5b77-1668-46f1-9089-e1691c6ff332'
    }

    try:
        response = requests.request("POST", url, headers=headers, json=payload, timeout=10)
        response_json= response.json()
        price = response_json['rate']
        print(type(price))
        price = float("%.2f"%(price))
        print(price)
        response.raise_for_status()
        return response.json(), price 
    
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error: {http_err}')
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error: {conn_err}')
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f'Connection Timeout: {timeout_err}')
        return None
    except requests.exceptions.RequestException as req_err:
        print(f'Error: {req_err}')
        return None

def crypto_currency_price(data, price):
    if data is None:
        print("Data is None. Request was not successful.")
        return
 
    if price is not None:
        low_price = float(1.17)
        max_price = float(6)
        print(f'Current price: {price}')
        if price <= low_price:
            print(f'The price is {price} low, time to buy!')
        elif price >= max_price:
            print(f'The price is {price} high, time to sell!')
        else:
            print(f'The price is {price}, no action needed.')
    else:
        print(f'Price not found for {price}.')
        
def crypto_monitoring():
    data, price = crypto_currency_request()
    print(data)
    crypto_currency_price(data, price)

crypto_monitoring()
