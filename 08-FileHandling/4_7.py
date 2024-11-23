import re
text = input('Enter your text: ')
pattern = r'[aeiouy]'
vovels = 0
match_letters = re.match(pattern, text)
for char in text:
    if match_letters:
        vovels += 1
    else:
        vovels += 0
print(vovels)