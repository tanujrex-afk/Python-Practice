total_bill=0.0
print("----------Retail billing system----------")
print("enter the price of each item, type 0 when you are finished\n")
while True:
    user_input = input("enter the item price(or 0 to complete):").strip()
    is_valid_number = user_input.replace('.','',1).isdigit()
    if not is_valid_number:
        print("invalid entry. please enter a valid numerical value")
        continue
    price = float(user_input)
    if price == 0:
        break
    total_bill += price
print("\n========")
print(f"Final bill amount:${total_bill:,.2f} ")
print("========")