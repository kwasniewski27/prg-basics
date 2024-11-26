paragraph = "cat dog mouse cat rat cat mouse"
dictionary = {}
words = paragraph.split()
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1 
for word, count in dictionary.items():
    print(f"{word} appears in text {count} times")