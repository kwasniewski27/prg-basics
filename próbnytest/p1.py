def f(player1, player2):
    total1 = 0
    total2 = 0
    for item in player1:
        if item == 'A':
            total1 += 10
        elif item == 'Q':
            total1 += 10
        elif item == 'J':
            total1 += 10
        elif item == 'T':
            total1 += 10
        elif item.isdigit():
            total1 += int(item)
    for item in player2:
        if item == 'A':
            total2 += 10
        elif item == 'Q':
            total2 += 10
        elif item == 'J':
            total2 += 10
        elif item == 'T':
            total2 += 10
        elif item.isdigit():
            total2 += int(item)
    if total1 >= total2:
        return True
    else:
        return False
print(f("AJ972","AQT72"))#False 
print(f("9532","K8"))