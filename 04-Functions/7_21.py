def f(number1,number2,number3):
    max_value = max(number1,number2,number3)
    min_value = min(number1,number2,number3)
    result = max_value - min_value
    return result
print(f(6,9,3))
print(f(9,8,7))