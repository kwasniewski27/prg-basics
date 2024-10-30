def f(n):
    if n != 0:
        asterisk = int(n-1) * '*/' + '*'
    if n == 0:
        asterisk = ''
    return asterisk
print(f(4))
print(f(0))