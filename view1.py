import numpy as np
arr_orig1=np.array([10,40,60])
arr_copy=arr_orig1.copy()
arr_copy[0]=300
arr_orig2=np.array([10,20,30])
arr_view=arr_orig2.view()
arr_view[0]=500
print("\n-----View Test------")
print("original:",arr_orig2)
print("view:",arr_view)
