arr = [-15, 8, -31, 47, -2, 19]
max_num = arr[0]
min_num = arr[0]
for i in arr:
    if i>max_num:
        max_num = i
    elif i<min_num:
        min_num = i
print('Największa liczba to:', max_num)
print('Najmniejsza liczba to:', min_num)