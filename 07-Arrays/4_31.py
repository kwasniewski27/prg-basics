arr = [
    [-38, 19], 
    [5, 40],
    [-7, 11],
    [29, 16]
]
arr2 = []
for i in arr:
    for j in i:
        arr2.append(j)
large = max(arr2)
small = min(arr2)
for i in range (len(arr)):
    for j in range (len(arr[i])):
        if arr[i][j] == small:
            print(f"Smallest {small} in {i+1} row and {j+1} column")
        if arr[i][j] == large:
            print(f"Largest {large} in {i+1} row and {j+1} column")