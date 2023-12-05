x = int(input("enter a number:"))
if (x % 2 == 0):
    print("x is even")
    x = int(input("enter a number:"))
elif (x % 2 != 0):
    print("x is odd")
    x = int(input("enter a number:"))
else:
    print("None")