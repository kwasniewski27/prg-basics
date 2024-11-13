def compare(array1, array2):
    if array1!=array2:
        print('Arrays are different')
    elif array1==array2:
        print('Arrays are the same')
arr1 = ["water","book","sky"]  
array1 = ["water","book","sky"]
arr2 = [True,False]
array2 = [True,False,True]
arr3 =  [5,3,1]
array3 = [5,3,1]
arr4 =  [3,2,1]
array4 = [3,2]
print('Array1:', arr1)
print('Array2:', array1)
print(compare(arr1,array1))
print('Array1:', arr2)
print('Array2:', array2)
print(compare(arr2,array2))
print('Array1:', arr3)
print('Array2:', array3)
print(compare(arr3,array3))
print('Array1:', arr4)
print('Array2:', array4)
print(compare(arr4,array4))