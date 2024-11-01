def sum_natural(n):
    count = 0
    for digit in range(1, n):
        count += int(digit)
    return count
print(sum_natural(10))