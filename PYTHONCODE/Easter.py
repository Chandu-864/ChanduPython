def Easter():
    Year = int(input("Enter a year btw (1982 to 2048): "))
    if 1982 <=Year <= 2048:
        a = Year % 19
        b = Year%4
        c = Year%7
        d = ((19*a) + 24) % 30
        e = ((2*b) + (4*c) + (6*d) + 5)%7
        easter = 22 + d + e
        if easter > 31:
            easter =easter-31 
            print("The date of Easter is April",easter,Year)
        else:
            print("The date of Easter is March",easter,Year)
Easter()