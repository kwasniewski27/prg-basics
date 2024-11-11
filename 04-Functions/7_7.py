def f(binary_number):
    binary_number = str(binary_number)
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True
print(f("101101"))
print(f("1311a10100"))