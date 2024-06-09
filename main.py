# LAB
price=2.99
quantity=3
tax_rate=7.5/100
subtotal=price*quantity
tax=subtotal*tax_rate
total=tax+subtotal
print(f"```\nprice of item: ${price}\nQuenitiy: {quantity}\nTax rate: {tax_rate*100}%\nSubtotal: ${subtotal}\nTax: ${round(tax,2)}\nTotal: ${round(total,2)}\n```")
