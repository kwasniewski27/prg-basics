def f(name):
    names = name.split()
    acronym = ''
    for name in names:
        for char in name:
            if char == name[0]:
                acronym += char
    return acronym
print(f("Internet of Things"))
print(f("For Your Information"))