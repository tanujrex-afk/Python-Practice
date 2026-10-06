try:
    age_input = input("Enter your age:")
    age= int(age_input)
    print(f"your age is:{age}")
except ValueError:
    print("iNVALID AGE")
    