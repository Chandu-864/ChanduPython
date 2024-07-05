import math
def tri():
    a = float(input("Enter the side a for triangle: "))
    b = float(input("Enter the side b for triangle: "))
    c = float(input("Enter the side c for triangle: "))
    s = (a + b + c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The Area of triangle is: ",A)
    return A 
tri()