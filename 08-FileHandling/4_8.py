import re
def display_file(name):
    with open(name) as file:
        lines = file.readlines()
    # Wzorzec do dopasowywania liter (małe i duże litery oraz cyfry)
    pattern = r'[a-zA-Z0-9]'
    # Iterowanie przez linie i wypisywanie ostatnich czterech liter z każdej
    for line in lines:
        # Usuwamy znaki nowej linii, jeśli są
        line = line.rstrip()
        # Wybieramy ostatnie cztery znaki
        last_four = line[-4:]
        # Dopasowanie wzorca do ostatnich czterech znaków
        match_pattern = re.findall(pattern, last_four)
        # Sprawdzanie, czy dopasowaliśmy jakiekolwiek litery lub cyfry
        if match_pattern:
            print(f"Last four characters from line: {last_four} -> {''.join(match_pattern)}")
        else:
            print(f"Last four characters from line: {last_four} -> No valid characters found.")
# Nazwa pliku
name = 'files.txt'
display_file(name)
