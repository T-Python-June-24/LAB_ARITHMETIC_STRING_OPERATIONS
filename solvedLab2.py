price : float=3.5
quantity: int= 4
tax_rate: float=5 

tax: float
subtotal: float 
total_cost : float 
subtotal=price * quantity
tax= (tax_rate/100) * subtotal
total_cost= subtotal+tax
price_phrase=f"Price of item : $ {price}"
quantity_phrase=f"Quantity :{quantity}"
Tax_rate_phrase=f"Tax rate : {tax_rate} %"
subtotal_phrase=f"subtotal : $ {subtotal}"
tax_phrase=f"Tax: $ {tax}"
total_phrase=f"Total: $ {total_cost}"
print(",,,")

print(price_phrase)
print(quantity_phrase)
print(Tax_rate_phrase)
print("   ")
print(subtotal_phrase)
print(tax_phrase)
print(total_phrase)


print(",,,")