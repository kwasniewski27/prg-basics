def f(first_letter, last_letter):
    file_name = 'data.txt'
    with open(file_name, 'r') as file:
        dic = []
        content = file.read()
        lines = content.splitlines()
        for line in lines:
            if line[0] == first_letter and line[-1] == last_letter:
                dic.append(line)
        result = len(dic)
    return result
print(f('w','d'))