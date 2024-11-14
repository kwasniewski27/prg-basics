array = [15, 38, 7, 23, 14]
def f(number,array):
    if number in array:
        print(f'number {number} appears in the array')
    else:
        print(f'number {number} does not appear in the array')
f(23,array)
f(17,array)