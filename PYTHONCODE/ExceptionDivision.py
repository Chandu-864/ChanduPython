def main():

    print("This program gives the division and sum of of two numbers")

    while True:
        Number_1 = input("Enter a number(or press ENTER to quit):")
        if Number_1 == '':
            break
        Number_2 = input("Enter a number(or press ENTER to quit):")
        if Number_2 == '':
            break

        try:
            answerSUM = int(Number_1) + int(Number_2)
            print("__________________________________________________________")
            print("The Sum of input numbers is:",answerSUM)
            answerDIV = (float(Number_1) /float(Number_2))
        except ValueError:
            print("Please give numeric value for inputs")
        except ZeroDivisionError:
            print("You can't divide the number with 0, it gives infinity")
        else:
            print("The Division of input numbers is:",answerDIV)
            print("__________________________________________________________")

main()