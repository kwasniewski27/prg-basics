def f(palindrome):
    pal = palindrome[::-1]
    if palindrome == pal:
        return True
    else:
        return False
print(f("radar"))
print(f("12-11-21"))
print(f("book"))