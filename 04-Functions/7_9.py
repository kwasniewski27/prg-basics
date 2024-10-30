def f(number,even):
    evens = 0
    odd = 0
    for digit in str(number):
        digit = int(digit)
        if digit%2 != 0:
            odd += digit
        else:
            evens += digit
    if even:
        return evens
    else:
        return odd
print(f(3124,True))
print(f(3124,False))
print(f(20576,True))
print(f(20576,False))