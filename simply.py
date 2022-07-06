word = "SAI SRI BHARANI TARAKA RAM KUMAR"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
 if i % 2 == 0:
   converted_word += word2[i]
 else:
   converted_word += word1[i]
print("using converted-method::",converted_word)
print("With out using converted-method::",word)
