def leap():
    Year = int(input("Enter a year: "))
    if ( ((Year % 4) == 0) and ((Year %100) != 0)) or ( ((Year % 400) == 0)):
            print("This year is a leap year")
    else:
            print("This year is NOT a leap year")
leap()