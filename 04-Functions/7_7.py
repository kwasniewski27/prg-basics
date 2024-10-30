def f(binary_number):
    for x in binary_number:
        if x != '1' and x != '0':
            return False
    return True
        
print(f("101101"))
print(f("1311a10100"))