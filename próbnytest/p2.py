def f(arr):
    for i in range(0, len(arr)):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
print(f([7,7,7,7,7,5,7,7]))