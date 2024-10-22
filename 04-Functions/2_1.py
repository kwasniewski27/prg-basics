###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter letter: ")
print(f'Letter read from the keyboard is {letter}')

number = '20303'
number = int(number)
print(f'{number}')

decimal = 304
binary = bin(decimal)
print(f'{decimal} is {binary} in binary')

decimal = 304
hexadecimal = hex(decimal)
print(f'{decimal} is {hexadecimal} in hexadecimal')

sign = '€'
sign = ascii(sign)
print(f'€ is {sign} in integrer')

value = -17
new_value = abs(value)
print(f'Absolute value of {value} is {new_value}')

