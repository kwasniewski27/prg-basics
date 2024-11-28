matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
for row in matrix:
    for i in range(len(row)):
        matrix[i][i]=1
for row in matrix:
    print(row)