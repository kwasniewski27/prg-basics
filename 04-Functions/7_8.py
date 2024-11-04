def f(amount_to_pay):
    five = amount_to_pay//5
    two = (amount_to_pay - five*5)//2
    one = amount_to_pay - five*5 - two*2
    sum = five + two + one
    return  sum
print(f(23))
print(f(8))
print(f(2))
print(f(0))