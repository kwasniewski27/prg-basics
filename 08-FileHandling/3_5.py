###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter your username: ')
password = input('Enter your password: ')

# pattern (criteria) for username and password
username_pattern = r'^[a-z0-9]+$'
password_pattern = r'^[a-zA-Z0-9_]+$'

# check if username and password are ok
username_match = len(username)>=6 and re.match(username_pattern,username)
password_match = len(password)>=8 and re.match(password_pattern, password)

# print results
if username_match and password_match:
   print("Correct")
else:
   print("Invalid")