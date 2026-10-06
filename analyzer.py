regular_count = 0
defaulter_count = 0
print("------ Student attendance analyzer------")
print("please enter the attendance percentage for 5 students.\n")
for i in range(1,6):
    user_input = input(f"enter attendance percentage for student {i}:").strip()
    attendance =  float(user_input)
    if attendance < 75:
                print(f"->Student {i} Status: Defaulter X")
                defaulter_count += 1
    else:
         print(f"-> Student {i} Status: Regular Row ")
         regular_count += 1
print("\n====================")
print(" ATTENDANCE SUMMARY  ")
print("======================")
print(f"Total Regular Students : {regular_count}")
print(f"Total Defaulter Students : {defaulter_count}")
print("===========================")
