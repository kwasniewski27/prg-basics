def identity_matrix(n):
    rows = []
    for i in range(0,n):
        col = []
        for j in range(0,n):
            if i == j:
                col.append(1)
            else:
                col.append(0)
        rows.append(col)
    return rows
arr = identity_matrix(6)
for i in arr:
    for j in i:
        print(j, end = '')
    print()