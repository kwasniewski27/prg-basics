def f(amount_to_pay):
    
    if amount_to_pay == 0:
        return 0
    
    coins = [5, 2, 1]  # Coin denominations
    coin_count = 0

    for coin in coins:
        coin_count += amount_to_pay // coin  # Add the number of coins of this denomination
        amount_to_pay %= coin  # Update the remaining amount

    return coin_count
print(f(23))  
print(f(8))   
print(f(2))   
print(f(0))  