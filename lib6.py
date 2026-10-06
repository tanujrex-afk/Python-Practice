import numpy as np
import matplotlib.pyplot as plt
days=["Mon","Tue","Wed","Thu","Fri","Sat"]
hours=[5,6,8,4,3,1]
plt.grid()
plt.plot(days,hours,marker='o')
plt.title("Study hours per day")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()