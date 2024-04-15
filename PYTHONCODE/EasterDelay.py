def Easter():
    Year = int(input("Enter a year btw (1900 to 2099): "))
    if 1900 <=Year <= 2099:

        a = Year % 19
        b = Year%4
        c = Year%7
        d = ((19*a) + 24) % 30
        e = ((2*b) + (4*c) + (6*d) + 5)%7
        easter = 22 + d + e

        if Year == 1954 or 1981 or 2049 or 2076:
            easter =  22 + d + e - 7

        if easter > 31:
                easter =easter-31 
                print("The date of Easter is April",easter,Year)
        else:
                print("The date of Easter is March",easter,Year)
                
    else:
          print("Please enter a correct year btw (1900 to 2099)")
Easter()