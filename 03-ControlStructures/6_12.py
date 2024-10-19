number_of_products_purchased = int(input('Enter number of purchased products: '))
product_price = int(input('Enter amount: '))
if number_of_products_purchased >= 2:
    amount_to_pay = product_price*0.75
elif number_of_products_purchased < 2:
    amount_to_pay = product_price
print(f'You have to pay {amount_to_pay} PLN')