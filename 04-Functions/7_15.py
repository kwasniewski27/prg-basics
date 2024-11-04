def f(detector):
    total = 0
    max_total = 0
    for char in detector:
        if char == '+':
            total += 1
        elif char == '-':
            total -= 1
        max_total = max(max_total, total)
    if max_total>=3:
        return True
    else:
        return False
print(f("+-+++-+---"))
print(f("+-+-+-+-"))