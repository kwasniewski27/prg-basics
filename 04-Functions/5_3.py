from keyboard import input_string, input_integer, input_real, input_boolean

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter last name: ')
age = input_integer('Enter your age: ')
salary = input_real('Enter your salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name:{first_name}', (last_name))
print(f'age: {age}')
if not is_salary_hidden:
    print(f'Salary: {salary}')
else:
    print('Salary is hidden')