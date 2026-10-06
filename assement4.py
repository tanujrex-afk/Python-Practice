correct_password = "secret password"
user_input = ""
while user_input !=correct_password:
    user_input=input("enter the password:")
    if user_input!=correct_password:
        print("incorrect password, try again\n")
print("Access granted!")