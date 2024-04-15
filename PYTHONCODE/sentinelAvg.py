def Avg():
    Total = 0.0
    Count = 0
    X = int(input("Enter a number (below zero to quit): "))
    while X >= 0:
        Total = Total + X
        Count = Count + 1
        X = float(input("Enter a number (below zero to quit): "))
    print("The average for the numbers is",(Total/Count))
Avg()