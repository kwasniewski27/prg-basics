age = int(input('Enter age: '))
no_tax = age < 26
tax = age >= 26
print(f'Exemption from paying taxes: {no_tax}')
print(f'no exemption from paying taxes: {tax}')