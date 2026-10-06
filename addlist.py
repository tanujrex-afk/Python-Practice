def add_item(lst,item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list
food_stuff=['potato','tomato','mango','milk']
print(add_item(food_stuff,'meat'))
numbers = [2,3,7,9]
print(add_item(numbers,5))
