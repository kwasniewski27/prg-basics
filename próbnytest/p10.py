def f(array):
    min_value = array[0][0]
    min_col = -1
    min_row = -1
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]<min_value:
                min_value = array[i][j]
                min_col = i
                min_row = j
    if min_col == min_row:
        return True
    return False
print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))