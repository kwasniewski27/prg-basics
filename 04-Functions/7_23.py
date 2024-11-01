def f(password):
    if len(password)<6:
        return False
    used = set()
    for char in password:
        if char in used:
            return False
        used.add(char)
    return True
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
