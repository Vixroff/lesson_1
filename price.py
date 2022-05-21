def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    price_with_discount = price - price * discount / 100
    return(price_with_discount)

price_discounted = discounted(100,50)
print(price_discounted)