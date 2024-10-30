def f(card_number):
    hidden_card_number = card_number[0:2] + '*' * 10 + card_number[-4:]
    return hidden_card_number
print(f("5290312400019022"))