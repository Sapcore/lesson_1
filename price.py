price = 100
discount = 101


def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Discount value is too high!')
    if discount >= max_discount:
        price_with_dicount = price
    else:
        price_with_dicount = price - price * discount / 100
    return price_with_dicount


print(discounted(price, discount))

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)