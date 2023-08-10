number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
even=0
odd=0
while number >0:
    if number % 2 == 0:
        print(f"\nThe number {number} is even.")
        even=even+int(number)
        number = input("Enter a number, and I'll tell you if it's even or odd: ")
        number = int(number)

    elif number%2!=0:
        print(f"\nThe number {number} is odd.")
        odd=odd+int(number)
        number = input("Enter a number, and I'll tell you if it's even or odd: ")
        number = int(number)
    else:
        print('even')
        print('odd')