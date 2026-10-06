try:
    num1=float(input("first number"))
    operator=input("operator(+,-,*,/)").strip()
    num2=float(input("second number:"))
    if operator=='+':
        print(f"Result:{num1+num2}")
    elif operator=='-':
        print(f"Result:{num1-num2}")
    elif operator=='*':
        print(f"Result:{num1*num2}")
    elif operator=='/':
        print(f"Result:{num1/num2}")
    else:
        print("invalid operator")
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("cannot divide by zero")
