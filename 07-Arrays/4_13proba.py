def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False
arr = [1,2,3,4,5,6,7,8,9]
arr2 = [12,3,45,65,11]
print(occurs(6,arr))
print(occurs(5,arr2))
array = [15, 38, 7, 23, 14]
number = int(input('Enter your number: '))
if number in array:
    print(f'Number {number} appears in array')
else:
    print(f'Number {number} is not in array')