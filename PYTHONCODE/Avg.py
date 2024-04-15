def Avg():
    N = int(input("How many numbers do you have? "))
    Total = 0.0
    for X in range(N):
        X = float(input("Enter a number"))
        Total = Total + X
    print("The average for the numbers is",(Total/N))
Avg()