def f(x,y):
    count = 0
    for number in range (x,y):
        if number<0 and number%2 != 0:
            count += 1
    return count
print(f(-7,8))
print(f(-1,11))