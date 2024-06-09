
sentence:str = "I had a cat named knight, but three years ago he got eaten by a racoon - this is a true story."
word = "racoon"

#length of sentence
length = len(sentence)
print(length)

# index of first occurence of a word (five)
index = sentence.find(word)
print(index)

#count number of times word appears in the sentence
count = sentence.count(word)
print(count)

#sentence in uppercase
print(sentence.upper())

#sentence in lowercase
print(sentence.lower())

#replace word
new_word = "eagle"
new_sentence =  sentence.replace(word, new_word)

print(new_sentence)

#print last character of the sentence 
print(sentence[-1])

