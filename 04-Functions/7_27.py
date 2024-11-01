def f(product_code):
    last_digit = int(product_code[3])
    first_three = product_code[:3]
    suma = sum(int(digit) for digit in first_three)
    if suma%7== last_digit:
        return True
    else:
        return False
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))