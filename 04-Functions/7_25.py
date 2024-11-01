def f(x,y):
    count = 0
    for i in range (x,y+1):
        if i%2 == 0 and i%3 == 0 and i%4 !=0:
            count += i
        else:
            continue
    return count
print(f(1,20))
print(f(10,30))