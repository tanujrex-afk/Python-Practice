def find_even_numbers(n):
    even=[]
    for i in range(n+1):
        if i%2 !=0:
            even.append(i)
    return even
print(find_even_numbers(10))
