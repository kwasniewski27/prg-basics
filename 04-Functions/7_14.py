def f(number1,number2,operator):
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '%':
        result = number1%number2
    elif operator == '*':
        result = number1*number2
    elif operator == '**':
        result = number1**number2
    else:
        result = print('Wrong operator')
    return result
print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))