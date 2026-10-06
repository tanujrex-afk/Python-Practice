def sum_of_odd(n):
    total = 0
    for i in range(1,n+1):
        if i%2!=0:
            total+=i
    return total
print(sum_of_odd(5))
print(sum_of_odd(15))
print(sum_of_odd(105))