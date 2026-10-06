num=int(input("enter a number:"))
factorial =1
if num<0:
    print("factorial does not exist for a negative number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print("the factorial of number:",factorial)
