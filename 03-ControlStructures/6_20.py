decimal = int(input('decimal number: '))
binary_number = ""
if decimal == 0:
    binary_number = '0'
else:
    while decimal>0:
        remainder = decimal % 2
        binary_number = str(remainder) + binary_number
        decimal //=2
print(f'Liczba binarna: {binary_number}')
