def f(product_code):
    product_code = str(product_code)
    first_three = product_code[:3]
    last = int(product_code[3])
    sum=0
    for char in first_three:
        char = int(char)
        sum += char
    return sum%7 == last
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))