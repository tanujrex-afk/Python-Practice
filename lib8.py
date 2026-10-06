import numpy as np
import matplotlib.pyplot as plt
months=["Jan","Feb","Mar","April"]
sales=[100,120,150,170]
profit=[200,500,1200,2000]
plt.grid()
#plt.scatter(sales,profit)
plt.bar(sales,profit)
plt.title("Sales Report")
plt.xlabel("sales")
plt.ylabel("profit")
#plt.plot(months,sales,label="sales")
#plt.plot(months,profit,label="profit")
plt.legend()
plt.show()