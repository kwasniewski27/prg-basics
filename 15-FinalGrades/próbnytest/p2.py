def f(arr):
    for x in range(0, len(arr)):
        if arr[x]!=arr[x+1] and arr[x] != arr[x-1]:
            return arr[x]
print(f([7,7,7,7,7,5,7,7]))
print(f([6,2,2,2,2,2,2]))