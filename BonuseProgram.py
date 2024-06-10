sentence = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation."
word= "programming"

print(len(sentence))
print(sentence.find(word))
print(sentence.count("is"))
print(sentence.upper())
print(sentence.lower())

sentence = sentence.replace("Python", "C#")
print(sentence)
print(sentence[-1])
