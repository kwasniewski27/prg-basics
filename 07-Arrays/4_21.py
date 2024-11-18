def is_subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set1.issubset(set2)

arr1 = [2, 4, 6]
arr2 = [1, 2, 3, 4, 5, 6]

result = is_subset(arr1, arr2)
print(result)