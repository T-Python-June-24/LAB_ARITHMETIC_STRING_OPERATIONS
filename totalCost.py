price = 2.99
quantity = 3
tax_rate = 7.75 / 100
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}" )
print(f"Total: ${total}")