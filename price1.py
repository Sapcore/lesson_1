def format_price(price):
    if type(price) not in (int, float):
        raise TypeError('Enter value!')
    else:
        price = int(price)
        return price


my_price = 56.24
message = f'Price: {format_price(my_price)} rub.'
print(message)
int_price = format_price(my_price)
print(int_price)
