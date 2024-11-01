def f(expression):
    result = 0
    current_number = 0
    current_operator = '+'
    for char in expression:
        if char.isdigit():
            current_number = int(char)
        if char in '+-' or char== expression[-1]:
            if current_operator == '+':
                result += current_number
            elif current_operator == '-':
                result -= current_number
            current_operator = char
            current_number = 0
    return result
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))