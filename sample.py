import matplotlib.pyplot as plt
students=["Asha","Rahul","John","Priya","Kiran"]
marks=[85,72,90,65,78]
plt.grid()
plt.title("Chart of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.plot(students,marks)
plt.bar(students,marks)
plt.scatter(students,marks)
plt.savefig("sample.png")
plt.show()