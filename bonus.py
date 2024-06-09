programming_lang = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
word_in_santance = "Python"
index = programming_lang.find(word_in_santance)
count = programming_lang.count(word_in_santance)
programming_lang_upper = programming_lang.upper()
programming_lang_lower = programming_lang.lower()
old_word = "Python"
new_word = "php"
updated_sentance = programming_lang.replace(old_word,new_word)
last_char_in_sentanece = programming_lang[-1]
print(last_char_in_sentanece)
print(f" the sentance :{programming_lang} \n the length of sentance :{len(programming_lang)}\n the index of word python : {index} \n the number of python in the sentance: {count} \n the sentance in upper case: {programming_lang_upper}\n the sentance in lower case: {programming_lang_lower} replced word in sentance : {updated_sentance}\n the last char in the sentance: {last_char_in_sentanece}")
