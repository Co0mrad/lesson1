def format_price(price):
    price = int(price)
    price = str(price)
    return (f"Цена: {price} руб.")
x = format_price(56.24)
print(x)