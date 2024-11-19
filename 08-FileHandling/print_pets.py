def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
x = file_content.split()

# calculates the total number of cars parked
total = len(x)

print('Total words:', total)