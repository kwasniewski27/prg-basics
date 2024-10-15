basic_salary = 5000
is_bonus = str(input('is bonus? False/True:'))
bonus = 0.3 * basic_salary
if is_bonus == True:
    total_salary = basic_salary + bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')