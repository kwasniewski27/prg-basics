paragraph = "cat dog mouse cat rat cat mouse"
dic = {}
words = paragraph.split()
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for word, count in dic.items():
    print(f'Wyraz {word} wystepuje w tekscie {count} razy')