import time
your_number = int(input('input your number: '))
count = your_number
while count > 0:
    print(count)
    count -= 1
    time.sleep(0)
    if count == 5:
        print('five')
    elif count == 4:
        print('four')
    elif count == 3:
        print('three')
    elif count == 2:
        print('two')
    elif count == 1:
        print('one')
    elif count == 0:
        print('time is up')