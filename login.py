correct_pin = "1234"
max_attempts = 3
attempts = 0
access_granted = False

while attempts < max_attempts:
    user_pin = input("enter your 4 digit pin:")
    attempts +=1
    if user_pin == correct_pin:
        print("Access granted")
        access_granted = True
        break
    else:
        print("wrong pin")
    if attempts == 3:
        print("card blocked")