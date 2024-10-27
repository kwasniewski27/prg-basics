def f(detector):
    current_count = 0
    max_count = 0
    for sign in detector:
        if sign == "+":
            current_count +=1
        elif sign == "-":
            current_count -= 0
        max_count = max(max_count, current_count)

    return max_count >=3
print(f('+++++---+'))