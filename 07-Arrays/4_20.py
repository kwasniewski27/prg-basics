def f(arr):
    evens = [num for num in arr if num%2 == 0]
    odd = [num for num in arr if num%2 != 0]
    return evens + odd
arr = [7, 9, 2, 4, 5, 6]
result = f(arr)
print(result)