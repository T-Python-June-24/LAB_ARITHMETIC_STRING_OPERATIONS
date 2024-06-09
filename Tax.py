Price = 2.99
Quantity = 3
TaxRate = 0.075
Subtotal = Price * Quantity
Tax = Subtotal * TaxRate
Total = Subtotal + Tax

print("Price:",Price)
print("Quantity:",Quantity)
print("Tax Rate:",TaxRate)

print("\nSubtotal: $",Subtotal)
print("Tax: $",round(Tax,2))
print("Total: $",round(Total,2))

Sentence = "I'm enjoying the Python web development course which is given by Mr. Aqeel Aleid at Tuwaiq Academy in Riyadh"
Word = "Riyadh"

print(len(Sentence))
print(Sentence.index(Word))
print(Sentence.count(Word))
print(Sentence.upper())
print(Sentence.lower())
print(Sentence.replace(Word,"The Capital"))
print(Sentence[-1])