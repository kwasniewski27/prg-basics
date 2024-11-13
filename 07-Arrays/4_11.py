def function_bubblesort(array):
    n=len(array)
    for i in range(n):
        for j in range( 0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
array1=[64, 25, 12, 22, 11]
array2=[89,17,54,63,1]
array3 = [4,36,12,28,9,44,5]
print(function_bubblesort(array1))
print(function_bubblesort(array2))
print(function_bubblesort(array3))