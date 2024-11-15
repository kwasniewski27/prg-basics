array = [7,3,8,5,2]
def bubble(array):
    n = len(array)
    for i in range (n):
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
posortowane = bubble(array)
print(bubble(array))
print(posortowane[-2])