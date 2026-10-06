try:
    num1=float(input("enter first number:"))
    num2= float(input("enter second number:"))
    result = num1/num2
    print(f"result is:{result}")
except ValueError:
    print("error: please enter a valid number")
except ZeroDivisionError:
    print("error: cannot divide by zero")
    