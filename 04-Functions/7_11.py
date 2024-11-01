def f(x,y):
    total = 0
    for i in range(x,y):
        if i < 0  and i % 2 ==0:
            total += 1
        else:
            continue
    return total
print(f(-7,8))
print(f(-1,11))