def f(number):
    number = str(number)
    seen = set()
    doubles = set()
    for digit in number:
        digit = int(digit)
        if digit in seen:
            doubles.add(digit)
        else:
            seen.add(digit)
    return sum(doubles)
print(f(1027))
print(f(230335))
print(f(513553007))