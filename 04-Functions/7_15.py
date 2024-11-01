def f(detector):
    total = 0
    max_total = 0
    for sign in detector:
        if sign == '+':
            total +=1
        elif sign == '-':
            total -=1
        max_total = max(max_total, total)
    return max_total>=3
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))