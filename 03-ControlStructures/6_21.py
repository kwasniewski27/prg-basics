
amount = int(input('Enter the amount in PLN: '))
print(f'The amount of PLN {amount}is in coins: ')
if amount>5:
    coins5 = amount/5
    coins5 = int(coins5)
    rest = amount - coins5*5
    coins2 = rest/2
    coins2 = int(coins2)
    second_rest = amount - coins5*5 + coins2*2
    coins1 = amount - coins5*5 - coins2*2
elif amount < 5:
    coins5 = 0 
    coins2 = amount/2
    coins2 = int(coins2)
    second_rest = amount - coins5*5 + coins2*2
    coins1 = amount - coins2*2
print(f'5 PLN coins: {coins5}')
print(f'2 PLN coins: {coins2}')
print(f'1 PLN coins: {coins1}')