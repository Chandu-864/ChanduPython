import math
def main():
    print("This program gives the real solutions to quadriatic")
    print()

    a = float(input("enter coefficient a: "))
    b = float(input("enter coefficient b: "))
    c = float(input("enter coefficient c: "))
    discRoot = math.sqrt(b*b - 4*a*c)
    root1 = (-b + discRoot)/(2*a)        # x = (-b+/- sqrt(b^2 - 4ac))/(2a)  Quadriatic equation 
    root2 = (+b + discRoot)/(2*a)               

    print("The solutions are:",root1, root2)

main()
