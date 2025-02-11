import requests
# Requests is a library that allows you to get from a URL
book = requests.get('https://www.gutenberg.org/cache/epub/345/pg345.txt')
#print(book.text)
lines = book.text.split('\n')
punctuation_remove = ',.!?;'
punctuation_space = "\"',(),+-"
unique_words = {}
for line in lines:
    # remove punctuation
    for c in punctuation_remove:
        line = line.replace(c, "")
    for c in punctuation_space:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) + 1

print(unique_words)
print(unique_words['the'])
print(unique_words['dracula'])
print(unique_words['mina'])
print(unique_words['helsing'])
print(unique_words['jonathan'])




