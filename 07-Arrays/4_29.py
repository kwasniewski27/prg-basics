def create_2d_arr(x,y):
    rows = []
    for i in range(0,x):
        col = []
        for j in range(0,y):
            col.append(0)
        rows.append(col)
    return rows

arr = create_2d_arr(2,5)

for i in arr:
    for j in i:
        print(j, end=" ")
    print()