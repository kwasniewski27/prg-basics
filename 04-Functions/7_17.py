def f(palindrome):
    pal = palindrome[::-1]
    if pal == palindrome:
        return True
    else:
        return False
print(f("radar"))
print(f("12-11-21"))
print(f("book"))