import sys
correct_pin= "1234"
balance = 1000.00
remaining_attempts = 3
current_state = "LOGIN"
while True:
   if current_state == "LOGIN":
        user_pin= input("enter your (1-4):")   
        print()
        if choice == 1:
                    print(f"your current balance is:${balance:.2f}\n")
        
        elif choice == 2:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                        balance += amount
                        print(f"${amount:.2f} deposited succesfully!\n")
            else:
                        print("invalid amount.\n")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <=0:
                print("Invalid amount. please enter a positive number.\n")
            elif amount > balance:
                        print("insufficient funds!\n")
            else:
                        balance -= amount
                        print(f"${amount:.2f} withdrawn succesfully!\n")
        elif choice == 4:
            print("Thank you for using the ATM. please visit again\n")
            sys.exit()
        else:
             print("Invalid choice. please selec 1,2,3, or 4.\n")   
#def login_phase():
  #    remaining_attempts = 3
 #     while remaining_attempts > 0:
   #         user_pin = input("enter your 4 digit pin:")
    #        if user_pin == correct_pin:
     #           print("Access Granted\n")
      #          atm_menu()
       #        remaining_attempts -= 1
        #    if remaining_attempts > 0:
         #       print(f"wrong pin. you have {remaining_attempts} attempts left.\n")
          #  else:
           #     print("wrong pin. card blocked")
            #sys.exit()
login_phase()

        
        