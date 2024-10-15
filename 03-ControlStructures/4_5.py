###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    number = ord(char)
    new_number = number + 1
    char = chr(new_number)
    encrypted_text += char
print(f'plain text: {plain_text}')
print(f'enscrypted text: {encrypted_text}')
#Uif!fbsmz!cjse!dbudift!uif!xpsn