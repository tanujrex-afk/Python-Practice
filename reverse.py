num=int(input("enter an integer:"))
reversed_num=0
original_num=num
while num>0:
    remainder = num%10
    reversed_num=(reversed_num*10)+remainder
    num//=10
print("reversed_number=",(reversed_num))
if original_num==reversed_num:
    print(f"{original_num} is a palindrome number")
else:
    print(f"{original_num} is not a palindrome number")