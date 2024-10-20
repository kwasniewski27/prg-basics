for i in range(1,31):
    if i/3 == int(i/3) and i/5 == int(i/5):
        print('BINGO')
    elif i/3 == int(i/3):
        print('THREE')
    elif i/5 == int(i/5):
        print('FIVE')
    else:
        print(i)