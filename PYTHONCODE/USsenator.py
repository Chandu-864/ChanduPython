def Senate():
    Age = int(input("Enter your age: "))
    Citizen = int(input("Enter your years being U.S citizen: "))
    if Age >= 30 and Citizen >= 9:
        print("You are eligible for BOTH US Senate and US representative")
    elif 30> Age >= 25 and 9>Citizen >= 7:
        print("You are eligible for US representative") 
    else:
        print("You are NOT eligible for both US Senate and US representative")
Senate()