import re
file_name = 'email.txt'
with open(file_name, 'r') as file:
    lines = file.readlines()
sender_eadress_pattern = r'^(/w+) (@exaple.com)+$'
for line in lines:
    if sender_eadress_pattern in line:
        print(line)