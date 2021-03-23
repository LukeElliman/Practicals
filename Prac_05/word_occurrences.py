"""Count word occurences in a string"""

word_to_count = {}
# text = str(input("Text: "))
text = "this is a collection of words of nice words this is a fun thing it is"

words = text.split()
for word in words:
    amount = word_to_count.get(word, 0)
    word_to_count[word] = amount + 1

final_words = list(word_to_count)
for word in final_words:
    print("{0} : {1}".format(word, word_to_count[word]))
