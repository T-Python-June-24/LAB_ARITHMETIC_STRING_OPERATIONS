ten_words = "Zero One Two Three Four Five Six Seven Eight Nine"
four = "Four"
print(len(ten_words))
print(ten_words.find(four))
print(ten_words.count(four))
print(ten_words.upper())
print(ten_words.lower())
ten_words.replace(four, "Not Four")
print(ten_words[len(ten_words) - 1])