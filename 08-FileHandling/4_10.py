import csv
file_name = 'clothing.csv'
with open(file_name, newline = '')as csvfile:
    csvreader = csv.reader(csvfile)
    head = next(csvreader)
    for line in csvreader:
        if line[-2]<'60' and line[-1]<'40':
            print(line)