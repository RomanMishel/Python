currencies = {
    "USD" : 1.00,
    "JPY" : 149.50,
    "EUR" : 0.92,
}
def converter(amount):
    usd_amount = amount * currencies["USD"]
    jpy_amount = amount * currencies["JPY"]
    eur_amount = amount * currencies["EUR"]
    print(f"You have {usd_amount:.2f} in US Dollars\n {jpy_amount:.2f} in Japanese Yen\n {eur_amount:.2f} in Euros")

amount = float(input("Enter your amount of USD: "))
converter(amount)



