def f(player1, player2):
    count1 = 0
    count2 = 0
    for char in player1:
        if char == 'A':
            count1+= 10
        elif char == 'K':
            count1 += 10
        elif char == 'Q':
            count1 += 10
        elif char == 'J':
            count1 += 10
        elif char == 'T':
            count1 += 10
        else:
            count1 += int(char)
    for char in player2:
        if char == 'A':
            count2 += 10
        elif char == 'K':
            count2 += 10
        elif char == 'Q':
            count2 += 10
        elif char == 'J':
            count2 += 10
        elif char == 'T':
            count2 += 10
        else:
            count2 += int(char)
    if count1 >= count2:
        return True
    return False
print(f("AJ972","AQT72"))
print(f("9532","K8"))