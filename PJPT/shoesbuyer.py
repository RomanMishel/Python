from shoes import shoes

low = shoes("And1" , 30)
medium = shoes("Addidas", 50)
high = shoes("Nike", 100)

try:
    shoe_budget = float(input("What is your shoe budget? : "))

except ValueError:
    exit("Please enter a number!")

for shoes in [high, medium, low]:
    shoes.buy(shoe_budget)
    
exit('Thanks for using our shoe budget app!')
    