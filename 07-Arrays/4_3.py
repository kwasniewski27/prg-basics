arr = [8,2,5,1,9]
def second_power(arr):
    square = []
    for i in arr:
        square.append(i**2)
    return square
print(second_power(arr))