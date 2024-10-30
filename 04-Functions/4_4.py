def sum_digits(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total
number = int(input('Enter integer number: '))
number = abs(number)
number = str(number)
result = (sum_digits(number))
print(f'Sum digits of {number} is: {result}')