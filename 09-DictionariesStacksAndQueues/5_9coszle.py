import re
file = 'vehicle.txt'
file2 = 'province.csv'
dictionary = {}
with open(file,'r') as file:
    content1 = file.read()
with open(file2,'r') as file:
    content2 = file.read()
lines = file.split()
provinces = file2.splitlines()
for word in lines:
    for value in provinces:
        if lines[0]==provinces[0]:
            dictionary[provinces] += 1
print(dictionary)