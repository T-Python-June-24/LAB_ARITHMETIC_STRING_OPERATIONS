price:float = 3000
item:str = "phone"
quantity:int = 3
tax_rate:float = 15 # to make the code easy to edit 
tax_rate_decimal:float  = tax_rate/100 # tax rate as decimal 
tax_rate_decimal_percentage:float = tax_rate_decimal*100
subtotal:float = price * quantity
tax:float = round(subtotal * tax_rate_decimal,2)
total:float = round(subtotal + tax,2)
phrase = f" Price of {item}: {price} \n Quantity: {quantity} \n Tax rate: {tax_rate_decimal_percentage}% \n Subtotal: {subtotal} \n Tax: {tax} \n Total: {total}"
print(phrase)