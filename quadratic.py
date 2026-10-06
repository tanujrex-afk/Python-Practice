import math
def solve_quadratic(a,b,c):
    if a==0:
        return "coefficient 'a' cannot be zero in quadratic equation."
    discrimant = b**2-4*a*c
    if discrimant <0:
        return "no real solution"
    elif discrimant == 0:
        return{-b/(2*a)}
    else:
        root1=(-b+ math.sqrt(discrimant)/(2*a))
        root2=(-b-math.sqrt(discrimant)/(2*a))
    return{root1,root2}
print(solve_quadratic(15,20,0))