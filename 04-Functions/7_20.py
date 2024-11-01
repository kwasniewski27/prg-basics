def is_prime(num):
    if num<2:
        return False
    for x in range (2, num):
        if num%x ==0:
            return False
    return True
def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count +=1
    return num
print(f(1))
print(f(5))