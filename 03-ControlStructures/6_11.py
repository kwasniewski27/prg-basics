current_product_price = int(input('Enter current product price: '))
previous_product_price = int(input('Enter previous product price: '))
discount = 100 - current_product_price/previous_product_price*100
if current_product_price/previous_product_price*100 < 90:
    print('BUY THIS PRODUCT!!!')
    print(f'Product price reduced by {discount}%')
else:
    print('Nothing interesting')