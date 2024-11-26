translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input('Enter word to be translated: ')
if word in translations:
    print(f"{word} = {translations[word]}")
else:
    print(f'There is no such word as {word} in our translations')