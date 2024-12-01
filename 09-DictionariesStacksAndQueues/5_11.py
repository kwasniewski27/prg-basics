import json

# Definicja ścieżki do pliku z danymi głosów
file_name = 'voting.json'

# Funkcja do odczytu głosów z pliku
def read_votes():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Jeśli plik nie istnieje, zwrócimy pusty słownik
        return {}

# Funkcja do zapisania głosów do pliku
def save_votes(votes):
    with open(file_name, 'w') as file:
        json.dump(votes, file)

# Główna funkcja do obsługi głosowania
def vote():
    # Odczytujemy głosy z pliku
    votes = read_votes()

    # Prosimy użytkownika o wpisanie imienia osoby, na którą głosuje
    person_name = input('Na kogo głosujesz? Podaj imię osoby: ')

    # Jeśli osoba już ma głosy, zwiększamy ich liczbę, w przeciwnym razie dodajemy ją z jednym głosem
    if person_name in votes:
        votes[person_name] += 1
    else:
        votes[person_name] = 1

    # Zapisujemy zaktualizowane dane do pliku
    save_votes(votes)

    # Informujemy użytkownika o zaktualizowanej liczbie głosów
    print(f'Głos na {person_name} został zapisany. Łącznie ma {votes[person_name]} głosów.')

# Uruchomienie programu
if __name__ == "__main__":
    vote()
