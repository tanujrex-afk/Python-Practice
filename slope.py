import math
def calculate_slope(x1,y1,x2,y2):
    if x2-x1 == 0:
        return "undefined slope(vertical line)"
    return(y2-y1)/(x2-x1)
print(calculate_slope(10,20,5,15))