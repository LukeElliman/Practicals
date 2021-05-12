import wikipedia

search_word = input("Enter your search word ")

for word in wikipedia.search(search_word):
    print(word)


page = wikipedia.page(search_word)
try:
    print(wikipedia.summary(search_word))
except wikipedia.WikipediaException as error:
    print(error)
print(page.url)
print(page.images)