def date():
    Date = input("Enter the date in (month/day/year) format: ")
    month, day, year = Date.split("/")
    month, day, year = int(month), int(day), int(year)
    if 0 < month < 13:
        if 0 < day <= 31:
            if month in [4, 6, 9, 11] and day > 30:
                print("The date entered is invalid")
            elif month == 2:
                if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                    if day > 29:
                        print("The date entered is invalid")
                elif day > 28:
                    print("The date entered is invalid")
                else:
                    print("The date entered is valid")
            else:       
                print("The date entered is valid")
        else:
            print("The date entered is invalid")
    else:
        print("The date entered is invalid")
date()