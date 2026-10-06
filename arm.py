num=int(input("enter an integer:"))
total_sum=0
temp=num
while temp>0:
    digit=temp%10
    total_sum+=digit ** 3
    temp//=10
if num== total_sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")