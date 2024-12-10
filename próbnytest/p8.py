def f(expression):
    stack = []
    expression = expression.split()
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in '+-':
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '+':
                result = num1 + num2
            elif char == '-':
                result = num1 -num2
            stack.append(result)
    return stack.pop()
print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))