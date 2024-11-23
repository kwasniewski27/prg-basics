multiplication = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for i in range(5):
    for j in range(5):
        multiplication[i][j] = (i+1)*(j+1)
for rows in multiplication:
    print(rows)