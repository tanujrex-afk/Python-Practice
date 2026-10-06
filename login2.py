correct_pin= 1234
max_attempts = 3
#intialize
attempts = 0
access_granted=""
balance = 10000.00
#login phase
while attempts < max_attempts:
    user_pin = input("enter your 4 digit pin:")
    attempts+=1
    if user_pin == correct_pin:
        print("Access Granted\n")
        access_granted = True
        break
    else:
        print("Wrong pin\n")
        if not access_granted:
            print("Card Blocked\n")
# banking phase
while access_granted:
    print("====ATM Menu====")
    print("1.Check Balance\n")
    print("2.Deposit money\n")
    print("3.Withdraw Money\n")
    print("4.Exit\n")
choice = input("choose an option(1-4):")
if choice == 1:
    print(f"your current balance is:${balance:.2f}\n")
elif choice == 2:
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        balance +=amount
        print(f"${amount:.2f} deposited succesfully!\n")
    else:
        print("Invalid Amount.\n")
elif choice == 3:
    amount= float(input("Enter amount to withdraw: $"))
    if amount > balance:
        print("insufficent funds!\n")
    elif amount > 0:
        balance -=amount
        print(f"${amount:.2f} withdrawn succesfully!\n")
    else:
        print("invalid amount.\n")
elif choice == 4:
    print("thank you for using the ATM. visit again!")
    access_granted = True # breaks the menu loop
else:
    print("invalid choice. please seleect 1,2,3, or 4.\n")