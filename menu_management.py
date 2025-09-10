def add_item(menu, item):
    menu.append(item)
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
def check_item(menu, item):
    if item in menu:
        return f'"{item} is available"'
    else:
        return f'"{item} is not available"'
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
print("Updated menu:", menu)
print("Availability:", check_item(menu, "Pizza"))
