###
# Reads a non-existent file
#

# there is no file with this name on the disk
file_name = 'xyz.txt'

try:
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
    print('Podany plik nie istnieje')