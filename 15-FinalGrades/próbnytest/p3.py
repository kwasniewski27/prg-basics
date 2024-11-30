def f(array2d):
    total_col = 0
    total_row = 0
    for row in array2d:
        for i in row:
            total_col += row[i]
            total_row += i
            if total_col == total_row:
                return True
            return False
print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))