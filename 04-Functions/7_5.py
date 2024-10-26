from rangemodule import range
number = int(input('Enter number: '))
x = 2
y = 15
if range(number, x, y):
    print(f'A number {number}')
    print(f'number {number} in range <{x},{y}>: yes')
else:
    print(f'Number {number} is not in range <{x},{y}>: no')