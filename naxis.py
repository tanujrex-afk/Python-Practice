import numpy as np
marks=np.array([[80,70,90],
               [60,85,75],
               [90,95,88]])
print(np.sum(marks,axis=1))
print(np.mean(marks,axis=1))