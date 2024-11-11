def f(number, even):
    evens = 0
    odd = 0
    number = str(number)
    for digit in number:
        digit = int(digit)
        if digit %2 ==0:
            evens += digit
        elif digit %2 != 0:
            odd += digit
    if even:
        return evens
    else:
        return odd
print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))