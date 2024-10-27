def f(number):
    str_number = str(number)  
    repeated_sum = 0  
    seen = set()  
    repeated_digits = set()  
    for digit in str_number:
        if digit in seen:
            repeated_digits.add(digit)  
        else:
            seen.add(digit)  

    
    for digit in repeated_digits:
        repeated_sum += int(digit) * str_number.count(digit)  

    return repeated_sum
print(f(1027))
print(f(230335))
print(f(513553007))
