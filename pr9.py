pass_count=0
fail_count=0
for i in range(1,6):
    marks=int(input("enter the marks"))
    if marks >=35:
        pass_count+=1
    else:
       fail_count+=1
print("Failed students",fail_count)
print("passed students",pass_count)
