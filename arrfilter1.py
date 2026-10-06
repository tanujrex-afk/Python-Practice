import numpy as np
marks=np.array([45,78,92,34,88,67,95])
filter_arr=(marks>=70) & (marks<=90)
print(marks[filter_arr])