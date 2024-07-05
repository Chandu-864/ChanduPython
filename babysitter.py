def babysitter():
    S = float(input("Enter Starting time in (Hours.minutes)format: "))
    E = float(input("Enter Ending time in (Hours.minutes)format: "))
    H = E - S
    if E <= 21.00 and S >= 9.00:
        R = 2.5 # in dollars
        Bill =  H*R
        print("Your bill is: ",Bill,"$")
    else:
        R = 1.75
        Bill =  H*R
        print("Your bill is: ",Bill,"$")
babysitter()