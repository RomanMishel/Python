price = int(input("What is the price of product: "))
discount = int(input("What discount on this product: "))

discount = float(discount / 100)

discout_sum = price * discount
final_price = price - discout_sum
print(f"Your discount is {discout_sum:.2f}")
print(f"Your final price is {final_price:.2f}")