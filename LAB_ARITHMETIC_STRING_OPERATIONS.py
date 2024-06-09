price = 5.99
quantity = 6
tax_rate = 0.075
subtotal = price * quantity 
tax = subtotal * tax_rate
total = subtotal + tax
print("price of item: ${}".format(price))
print("quantity: {}".format(quantity))
print("tax_rate: % {}".format(tax_rate))

print("Subtotal: $ {}".format(subtotal))
print("Tax: $ {}".format(tax))
print("Total: ${}".format(total))