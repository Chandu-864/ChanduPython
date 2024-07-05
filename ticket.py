def ticket():
    MPH = float(input("Enter the speed(MPH) you drove: "))
    print("The Speed_limit is 40")
    if MPH > 40 and MPH < 90:
        T = 50 + ((MPH - 40)*5)
        print("This speed was Illegal")
        print("Speeding bill is",T,"$")
    elif MPH >90:
        T = 50 + ((MPH - 40)*5) + 200
        print("This speed was Illegal")
        print("Speeding bill is",T,"$")
    else:
        print("This speed was Legal")
        print("Thank you for maintaining Speed limit!")
ticket()