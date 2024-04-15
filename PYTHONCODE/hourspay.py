def main():
    H = float(input("How many hours have you worked: "))
    R = float(input("What is the rate of pay per 1 hour: "))
    if H <= 40:
        Wage = H*R
        print("The wage is ",Wage)
    elif H > 40:
        Extra_Wage = (40)*R +((H-40)*(R + (R/2)))
        print("The wage is ",Extra_Wage)
main()