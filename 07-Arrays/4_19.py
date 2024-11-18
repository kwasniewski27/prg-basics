def f(greater, array):
    total = 0
    for element in array:
        if element>greater:
            total += 1
    return total
print(f(7,[6,8,9,2,3,4,9]))