price:float = 49.95
print(f"Price of the item: ${price}")
quantity:int = 4
print(f"Quantity: {quantity}")
tax_rate:float = 0.15
print(f"Tax rate: {tax_rate * 100}%")
print()
subtotal:float = price * quantity
print(f"Subtotal: ${subtotal}")
tax:float = tax_rate * subtotal
print(f"Tax: ${tax}")
total:float = subtotal + tax
print(f"Total: ${total}")
