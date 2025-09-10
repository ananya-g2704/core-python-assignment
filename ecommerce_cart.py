def commerce(cart):
    if not cart:   
        return 0
    total = sum(cart.values())
    if len(cart) > 5:
        total = total * 0.9   
    return total
items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print("Total Price:", commerce(items))
