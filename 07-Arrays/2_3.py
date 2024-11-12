# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_cost = 0
for row in monthly_expenses:
    for item in row:
        if item == row[0]:
            food_cost += item

transport_cost = 0
for row in monthly_expenses:
    for item in row:
        if item == row[1]:
            transport_cost += item

utilities_cost = 0
for row in monthly_expenses:
    for item in row:
        if item == row[2]:
            utilities_cost += item
first_week = sum(monthly_expenses[0])
second_week = sum(monthly_expenses[1])
third_week = sum(monthly_expenses[2])
fourth_week = sum(monthly_expenses[3])

total = first_week + second_week + third_week + fourth_week
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_cost)
print('Transport:',transport_cost)
print('Utilities:',utilities_cost)
print('Week 1:',first_week)
print('Week 2:',second_week)
print('Week 3:',third_week)
print('Week 4:',fourth_week)
print('---------------')
print('TOTAL:',total)