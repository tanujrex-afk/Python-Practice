while True:
   try:
        num1 = float(input("enter the first number:"))
        operator = input("Operator(+,-,*,/)").strip()
        if operator not in["+","-","*","/"]:
            print("error:invalid operator chosen.Try again.")
            print("-"*20)
            continue
        num2 = float(input("second number:"))
        if operator =="+":
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
        print("Error: enter valid numeric values.")
   except ZeroDivisionError:
        print("Error:Cannot divide by zero.")
   print("-"*20)
   repeat=input("do you want to calculatge again? (yes/no):").strip().lower()
   if repeat!="yes" and repeat!="y":
        print("good bye!")
        break
   print("-"*20)