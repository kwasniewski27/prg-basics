def f(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    elif n>=2 :
        x =  f(n - 1) + f(n - 2)
    return x
print(f(5))
print(f(9))