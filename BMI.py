def bmi():
    W = float(input("Enter your weight in pounds: "))
    H = float(input("Enter your height in inches: "))
    bmi = (W * 720) / (H * H)
    print(bmi)
    if bmi >= 19 and bmi <= 25:
        print("Your are healthy")
    elif bmi <= 19:
        print("Your health is below the bmi range")
    else:
        print("Your health is above the bmi range")
bmi()