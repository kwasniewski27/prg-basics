arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for row in arr:
    if row[0]:
        for i in range (len(row)):
            row1 = [i for i in range (1,6)]
    elif row[2]:
        for i in range (len(row)):
            row = [i*2 for i in range (1,6)]
        print(row1 + row)