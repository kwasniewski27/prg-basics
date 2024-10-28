def f(password):
    if len(password)<6:
        return False
    seen = set()
    for char in password:
        if char in seen:
            return False
        else:
            seen.add(char)
        return True
print(f('ax15'))
print(f('book123'))
print(f('A2water3'))
print(f('qwerty'))
print(f(''))