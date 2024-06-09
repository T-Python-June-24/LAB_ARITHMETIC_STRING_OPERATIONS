price = 3.99
quantit = 4
tax_rate = 8.6/100

subtotal = price * quantit

tax= tax_rate * subtotal

total = subtotal + tax
result = "Price of item: $"+ f"{price:.2f}"+"\nQuantity: "+ f"{quantit}"+"\nTax rate: "+str(tax_rate*100)+"%\n\nSubtotal: $"+f"{subtotal:}"+"\nTax: $"+f"{tax:.2f}"+ "\n Total: $"+f"{total:.2f}"
print(result)
sentence = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics"

word = "interpreted"
print(len(sentence))

print(sentence.index(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(word ,"naif"))
print(sentence[-1])