# Bonus, create a new python file and do the following:

# Define a string variable containing a sentence with at least 10 words.
# Define a string variable containing a word that appears in the sentence.
# Print the length of the sentence.
# Print the index of the first occurrence of the word in the sentence.
# Print the number of times the word appears in the sentence.
# Print the sentence in all uppercase letters.
# Print the sentence in all lowercase letters.
# Replace the word in the sentence with a new word of your choice.
# Print the last character of the sentence.

sent:str = "I'm really enjoying programming and dealing with data!"

word:str = "data"

print(len(sent))
print(sent.index(word))
print(sent.count(word))
print(sent.upper())
print(sent.lower())
print(sent.replace(word, "DATA"))
print(sent[-1])