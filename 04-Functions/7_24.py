def f(expression):
    total = 0
    current_number = 0
    current_operation = '+'
    for char in expression:
        if char.isdigit():
            current_number = int(char)
        elif char in '+-':
            if current_operation == '+':
                total += current_number
            if current_operation == '-':
                total -= current_number
    if current_operation == '+':
        total += current_number
    if current_operation == '-':
        total -= current_number
    return total
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))