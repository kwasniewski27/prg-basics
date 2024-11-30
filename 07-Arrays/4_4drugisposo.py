arr = [-15, 8, -31, 47, -2, 19]
n = len(arr)
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
max_num = arr[-1]
min_num = arr[0]
print('Największa liczba to:', max_num)
print('Najmniejsza liczba to:', min_num)