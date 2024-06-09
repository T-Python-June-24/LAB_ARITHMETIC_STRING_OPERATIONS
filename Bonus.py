pargraph="Chess is one of the oldest and most popular board games. It is played by two opponents on a checkered board with specially designed pieces of contrasting colours, commonly white and black"
Search="Chess"
print(len(pargraph))
index=pargraph.find(Search)
print(index)
print(pargraph.count(Search))
print(pargraph.upper())
print(pargraph.lower())
#  Replacing the word in the sentence with a new word
pargraph=pargraph.replace(Search,"Football")
print(pargraph[-1])