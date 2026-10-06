def sum_of_even(n):
    total=0
    for i in range(1,n+1):
        if i%2==0:
            total+=i
    return total
print(sum_of_even(10))
print(sum_of_even(40))
print(sum_of_even(120))

