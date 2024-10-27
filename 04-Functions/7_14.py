def f(number1,number2,operator):
    if operator == "+":
        z = number1+number2
        return z
    elif operator == "-":
        z = number1 - number2
        return z
    elif operator == "*":
        z = number1*number2
        return z
    elif operator == "/":
        z = number1/number2
        return z
print(f(6,9,"+"))
print(f(78,9,"/"))