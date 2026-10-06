try:
    a= int(input("Enter first number:"))
    b=int(input("enter second number:"))
    result = a/b
except ValueError:
    print("enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Thank you")