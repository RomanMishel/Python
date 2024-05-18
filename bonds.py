import requests
from bs4 import BeautifulSoup
import time

soup = ""

def crypto_currency_request():
    send_req = requests.get("https://www.livecoinwatch.com/price/Toncoin-TONCOIN")
    try:
        response = requests.get(send_req, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error: {conn_err}')
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f'Conecction Timeout')
    except requests.exceptions.RequestException as req_err:
        print(f'Error:{req_err}')
        return None
    soup = BeautifulSoup(response.content,'html.parser')

def crypto_currency_price():
    low_price = float()
    max_price = float()
    price_find = soup.find('span',_class='price')
    print(price_find)
    if price_find >= low_price(1,1,7):
        print(f'The price is {price_find} low, time to buy!')
    elif price_find <= max_price(6,1,9):
        print(f'The price is {price_find} high, time to sell!')
    elif price_find is None:
        print("Could not find Price!")
    else:
        return
    
if __name__ == "__main__":
    crypto_currency_request
    crypto_currency_price
    