import csv
file_name = 'it_company.csv'
with open(file_name, newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
    head = next(csvreader)
    job = 'Graphic Designer'
    for line in csvreader:
        if job in line:
            print(f'{line[1]}, {line[0]}, {line[3]}')