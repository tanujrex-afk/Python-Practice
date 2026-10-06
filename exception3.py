nuumbers=[10,40,60,80,45]
try:
    index_input=input("enter an index(0-4):")
    index=int(index_input)
    print(f"value at index {index} is: {nuumbers[index]}")
except ValueError:
    print("Error: cannot print the value ,enter a correct value")
except IndexError:
    print("error: index out of range")
    