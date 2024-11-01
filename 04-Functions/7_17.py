def f(palindrome):
    pal = palindrome[::-1]
    return pal == palindrome
print(f("radar"))
print(f("12-11-21"))
print(f("book"))