def f(number,even):
    total = 0
    for digit in str(number):
        digit = int(digit)
        if (even and digit%2==0) or (not even and digit%2 != 0):
            total += digit
    return total
print(f(3124, True))    
print(f(3124, False))   
print(f(20576, False))  
print(f(20576, True))   
print(f(13115, True))