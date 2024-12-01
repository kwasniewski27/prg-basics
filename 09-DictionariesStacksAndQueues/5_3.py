translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input('Enter the word you want to translate in english: ')
if word in translations:
    print(f'{word} means {translations[word]}')
else:
    print('Ther is no such name in our translations')