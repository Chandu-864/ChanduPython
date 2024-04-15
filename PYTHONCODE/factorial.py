import math
def main():
    print("This will give the factorial of a number")
    n= int(input("Enter a natural number: "))
    fact=1
    for factor in range(n,1,-1):
        fact= fact*factor 
        print("The factorial of", n, "is", fact)
main() 