def hide(card_number):
    hidden_number = card_number[0:2] + 10 * '*' + card_number[-4:]
    return hidden_number
print(hide("5290312400019022"))