import json

person_name = input('Na kogo głosujesz? Podaj imię osoby: ')
file_name = 'voting.json'
with open(file_name, 'r', encoding='utf-8') as file1:
    votes = json.load(file1)
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] == 1
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(votes, file)
print(f'Głos na {person_name} został dodany. {person_name} ma teraz {votes[person_name]} głosów')