arr = [
    [1,2,3,4,5],
    [1,3,5,7,9],
    [2,4,6,8,0]
]
print('**BEFORE**')
for row in arr:
    print(row)
arr1 = [
    [1,2,3,4,5],
    [1,3,5,7,9],
    [2,4,6,8,0]
]
for i in arr1:
    for j in arr1:
        j[0], j[-1] = j[-1], j[0]
print('***AFTER***')
for row in arr1:
    print(row)