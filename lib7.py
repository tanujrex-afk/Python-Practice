import numpy as np
import matplotlib.pyplot as plt
tunit=[28,29,30,31,32]
time=[2,4,6,8,24]
plt.grid()
plt.plot(tunit,time,marker='o')
plt.plot(tunit,time,color="red")
plt.plot(tunit,time,linestyle='-.')
plt.plot(tunit,time,linewidth='8')
plt.show()