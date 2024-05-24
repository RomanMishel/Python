import requests
import json

def crypto_currency_request():
    url = "https://api.livecoinwatch.com/coins/single"
    
    payload = json.dumps({
    "currency": "TON",
    "code": "EQCajaUU1XXSAjTD-xOV7pE49fGtg4q8kF3ELCOJtGvQFQ2C",
    "meta": False
    })
    headers = {
    'content-type': 'application/json',
    'x-api-key': 'c2ea5b77-1668-46f1-9089-e1691c6ff332'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    
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

def crypto_currency_price(data):
    if data is None:
        print("Data is None. Request was not successful.")
        return

    
    for coin in data.get("data", []):
        if coin.get("symbol") == "TON":
            price = coin.get("price")
            if price is not None:
                low_price = 1.17 
                max_price = 6
                print(f'Current price: {price}')
                if price <= low_price:
                    print(f'The price is {price} low, time to buy!')
                elif price >= max_price:
                    print(f'The price is {price} high, time to sell!')
                else:
                    print(f'The price is {price}, no action needed.')
            else:
                print("Price not found for TONCOIN.")
            return 
    print("TONCOIN not found in the response data.")

def crypto_monitoring():
    data = crypto_currency_request()
    crypto_currency_price(data)

crypto_monitoring()
