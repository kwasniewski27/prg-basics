import random
number = random.randint(1,100)
your_number = int(input('Wpisz swoją liczbę: '))
while your_number != number:
    if your_number>number:
        print('big big big')
    elif your_number<number:
        print('chill chill guy')
    your_number = int(input('Wpisz swoją liczbę: '))
print('hahahah')