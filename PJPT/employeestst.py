from PJPT.employees import employees

e1 = employees("Bob", "Sales", "Director", 100000, 20)
e2 = employees("Linda","Executive", "CIO",150000, 10)

print(e1.name)
print(e2.role)
print(e1.eligable_for_retirement())