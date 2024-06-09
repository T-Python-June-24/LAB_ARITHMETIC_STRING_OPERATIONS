#- Define a string variable containing a sentence with at least 10 words.
str = "Hello, My name is Ahmed and i am 21 years old!"

# efine a string variable containing a word that appears in the sentence.
print(str[17:23])

# print length of the sentence
print(len(str))

# - Print the index of the first occurrence of the word in the sentence.
print(str.index("Ahmed"))

#- Print the number of times the word appears in the sentence.
print(str.count("a"))

# convert sentence to uppercase
print(str.upper())

# convert sentence to lowercase
print(str.lower())

# replace a word in the sentence
print(str.replace("Ahmed", "Abdullah"))

# print the last character in the sentence
print(str[-1])