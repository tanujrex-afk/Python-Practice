import matplotlib.pyplot as plt
activities=["Sleep","Wakeup","Study","College","Home"]
hours=[7,5,6,8,4]
plt.pie(hours,labels=activities,autopct="%1.1f%%")

plt.show()