def main() : 
    print("This program illustrates a chaotic function") 
    X = eval(input("Enter a number between 0 and 1: ") ) 
    for i in range(4) : 
        X = ((3.9) * ((X) * (1 - X)))
    print(X)
    for i in  range(4):
        X  = ((3.9) * ((X) - (X * X)))
    print(X)
    for i in range(4):
        X = (((3.9 * X)) - ((3.9) * (X * X)))
    print(X)
main()