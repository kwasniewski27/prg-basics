def f(x, y):
    count = 0
    for numer in range(x, y):
        if numer < 0 and numer % 2 == 0:
            count += 1
    return count
print(f(-7, 8))  
print(f(-1, 11)) 
