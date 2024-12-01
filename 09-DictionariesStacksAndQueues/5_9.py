import csv
file_name = 'vehicle.txt'
file_csv = 'province.csv'
dir = {}
with open(file_name, 'r')as file:
    content = file.read()
    lines = content.splitlines()
    with open(file_csv, newline = '') as csvfile:
        csvreader = csv.reader(file_csv)
        head = next(csvreader)
        for line in csvreader:
            if line[0] == lines[0]:
                if line[0] in dir:
                    dir[line[0]] +=1 
                else:
                    dir[line[0]] = 1
for word, count in dir.items():
    print(f'{word}:{count}')
