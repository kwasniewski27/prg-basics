number = int(input('Enter your number: '))
if number > 0:
    message = 'positive'
if number < 0:
    message = 'negative'
if number == 0:
 message = 'zero'
print(f'number {number} is {message}')