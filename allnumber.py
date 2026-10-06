def add_all_numbers(*args):
    total = 0
    for num in args:
        
        total +=num
    return total
print(add_all_numbers(5,10,7))