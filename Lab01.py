price = 3.67
print ("Price of item: $",price)

quantity = 6
print("Quantity: ",quantity)

tax_rate = 0.15
print("Tax rate: ",tax_rate,"%")

subtotal = price * quantity
print ("\nSubtotal: $",round(subtotal,2))

tax: float = tax_rate * subtotal
print ("Tax: $",round(tax,2))

total = subtotal + tax
print ("Total: $",round(total,2))


