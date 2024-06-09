price = 5.5
print(f"Price of item: ${price}")
quantity = 6
print(f"Quantity: {quantity}")
tax_rate =  0.15 # 15% tax rate
print(f"Tax rate: 15 % \n")
subtotal = price * quantity
print(f"Subtotal: ${subtotal}")

tax = subtotal * tax_rate
print(f"Tax 15%: ${tax}")

total = subtotal + tax
print(f"Total: ${total}")



