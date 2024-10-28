def f(expression):
    expression.replace(" ", "")
    total = 0
    current_number = 0
    operation = '+'
    for char in expression:
        if (char.isdigit()):
            current_number = int(char)
        if char in '+-' or char == expression[-1]:
            if operation == '+':
                total += current_number
            if operation == '-':
                total -= current_number
            operation = char
    return total
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))