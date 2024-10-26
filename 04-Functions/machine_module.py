def f(amount_to_pay):
    if amount_to_pay >=5:
        amount5pln = amount_to_pay/5
        amount5pln = int(amount5pln)
        amount2pln = (amount_to_pay - amount5pln*5)/2
        amount2pln = int(amount2pln)
        amount1pln = (amount_to_pay - amount5pln*5 - amount2pln*2)
        amount1pln = amount1pln
        sum = amount1pln + amount2pln + amount5pln
    elif amount_to_pay < 5 and amount_to_pay>=2 :
        amount2pln = int(amount_to_pay/2)
        amount1pln = amount_to_pay - amount2pln
        sum = amount1pln + amount2pln
    elif amount_to_pay < 2:
        amount1pln = int(amount_to_pay/1)
        sum = amount1pln
        print()