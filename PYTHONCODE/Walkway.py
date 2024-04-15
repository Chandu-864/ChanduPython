from random import random
def Toss():
    N = int(input("Enter the number of toss you will spin: "))
    S = 0
    F = 0
    B = 0
    toss = ['H', 'T']
    for _ in range(N):
        if random(toss) == 'H':
            F = F + 1
        elif random(toss) == 'T':
            B = B - 1
        S = F + B 
        print(S)
        average_F = (S/F)
        average_B = (S/B)
        print(average_F)
        print(average_B)
Toss()