password = input('Enter password: ')
password_ok = len(password) >= 8
password_wrong = len(password) <8
print(f'Password length is valid: {password_ok}')
print(f'Password length is wrong: {password_wrong}')