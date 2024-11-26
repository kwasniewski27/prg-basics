price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
total = 0
after_value = 0
for key,value in price_list.items():
    new_value = round(value*0.9 , 2)
    print(f"Before discount prices: {key} : {new_value}")
    total += value
    total = round(total,2)
    after_value += new_value
    after_value = round(after_value,2)
    print(f"After discount prices: {key}:{value}")
print(f"Total value before discount is: {total}")
print(f"Total value after discount is: {after_value}")