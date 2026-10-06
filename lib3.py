import numpy as np
import matplotlib.pyplot as plt
xaxis=np.array([1,2,6,8])
yaxis=np.array([3,8,1,10])
#plt.plot(xaxis,yaxis,linestyle='-')
#plt.plot(xaxis,yaxis,linestyle="--")
plt.plot(xaxis,yaxis,linestyle=":")
#plt.plot(xaxis,yaxis,linestyle="-.")
plt.plot(yaxis,linewidth='20.5')
plt.show()