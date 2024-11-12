categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_val = expenses.index(max(expenses))
for i in range(len(expenses)):
    if i == max_val:
        print(categories[i])