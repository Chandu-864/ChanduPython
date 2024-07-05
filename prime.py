N = int(input("Enter a positive number: "))
if N % 2 != 0 and N %3 != 0 and N % 5 != 0:
    print("Prime")
else:
    print("composite")