###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter your username: ')
password = input('Enter your password: ')

# pattern (criteria) for username and password
username_pattern = r'^[a-z]+$'
password_pattern = r'^[a-zA-Z0-9_]+$'

# check if username and password are ok
username_match = re.match(username_pattern,username) and len(username)<=6
password_match = re.match(password_pattern, password) and len(password)<=8

# print results
if username_match and password_match:
   print('Your username and password are ok')
else:
   print('Your username or/and password are wrong')