sal=0
highest=0
lowest=0
for i in range(1,6):
    salary= int(input("enter the salary"))
    sal=sal+salary
    average=sal/5
    if salary > highest:
        highest=salary
    if i == 1 or salary < lowest:
        lowest = salary
         
print("total salary=",sal)
print("avearge salary=",average)
print("hihest salary=",highest)
print("lowest salary",lowest)