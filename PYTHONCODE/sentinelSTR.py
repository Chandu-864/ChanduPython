def Avg():
    Total = 0.0
    Count = 0
    Xstr = input("Enter a number(or Enter to quit): ")
    while Xstr != "":
        X = float(Xstr)
        Total = Total + X
        Count = Count + 1
        Xstr = input("Enter a number(or Enter to quit): ")
    print("The Average for the numbers is",(Total/Count))
Avg()