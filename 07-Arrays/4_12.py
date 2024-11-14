arr = [2, 3, 2, 5, 8, 1, 9, 8]
def find_unique_elements(arr):
    unique_elements = []
    for digit in arr:
        if arr.count(digit)==1:
            unique_elements.append(digit)
    return unique_elements
print(find_unique_elements(arr))