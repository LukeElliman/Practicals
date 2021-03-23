"""Count word occurences in a string"""

word_to_count = {}
text = str(input("Text: "))

words = text.split()
for word in words:
    amount = word_to_count.get(word, 0)
    word_to_count[word] = amount + 1

final_words = list(word_to_count)
final_words.sort()

longest_word = max((len(word) for word in final_words))

for word in final_words:
    print("{0:{1}}:  {2}".format(word, longest_word, word_to_count[word]))

