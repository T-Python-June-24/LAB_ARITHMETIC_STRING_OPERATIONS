# step one 
price:int = 45

# step two
quantity:int = 3 

#step three
tax_rate:int = 15

# step four 
subtotal = (price * quantity)

# step five 
tax = subtotal * tax_rate/100

# step six 
total = subtotal + tax 

#step seven 
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%" )
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")