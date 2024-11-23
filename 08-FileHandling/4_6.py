import re
def dispaly_file(name):
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
        total_lines = len(lines)
        total_words = 0
        total_char = 0
        for line in lines:
            words = name.split()
            total_words += len(words)
            total_char += len(line)
        print(f'File name: {name}')
        print(f'Number of lines: {total_lines}')
        print(f'Number of words: {total_words}')
        print(f'Number of chars: {total_char}')
    except FileNotFoundError:
        print(f"Error: File '{name}' not found.")
name = input('Enter name of the file: ')
dispaly_file(name)