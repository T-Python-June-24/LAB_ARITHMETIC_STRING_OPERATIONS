str = "I would really love to travel to Norway this coming summer"
strAppeared = "love"

#Printing the length of the str.
print(len(str))

#Printing the index of the first occurrence of the word "love" in the sentence.
print(str.index(strAppeared))

#Printing the number of times the word "love" appears in the sentence.
print(str.count(strAppeared))

#Printing the sentence in all uppercase letters.
print(str.upper())

#Printing the sentence in all lowercase letters.
print(str.lower())

#Replacing the word, "love" in the sentence with the word, "like".
newStr = str.replace(strAppeared, "like")
print(newStr)

#Printing the last character of the sentence.
print(str[-1:])
