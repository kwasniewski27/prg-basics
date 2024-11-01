def is_prime(number):
    for x in range(2, number+1):
        if number<2:
            return False
        elif number%x == 0:
            return False
    return True
def f(n):
    count = 0
    num = 1
    while count < n:
        num +=1
        if is_prime(num):
            count += 1
    return num