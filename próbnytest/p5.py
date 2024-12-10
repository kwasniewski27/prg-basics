def f(first_letter, last_letter):
    file_name = 'data.txt'
    with open(file_name, 'r', encoding = 'utf-8') as file:
        dic = []
        content = file.read()
        lines = content.splitlines()
        for words in lines:
            if words and words[0] == first_letter and words[-1] == last_letter:
                dic.append(words)
        result = len(dic)
    return result
print(f("w", "d"))