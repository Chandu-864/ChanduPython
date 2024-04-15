def Avg():
    Total = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        X = float(input("Enter a number: "))
        Total = Total + X
        count = count + 1
        moredata = input("Do you have more numbers(Yes or No)? ")
    print("The average of numbers is",(Total/count))
Avg()