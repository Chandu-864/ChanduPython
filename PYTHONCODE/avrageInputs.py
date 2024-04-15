def main():
    Xstr = input("Enter a number( or press ENTER to quit): ")
    Total = 0
    Count = 0
    while (Xstr != ""):
        X = float(Xstr)
        Total = Total + X
        Count = Count + 1
        Xstr = input("Enter a number( or press ENTER to quit): ")
    print("The average for the numbers is:",(Total/Count))
main()