from random import random

def intro():
    print("This is a Craps casino game played with a pair of dice.")
    print("This will run the simulation for the player to win or lose a game.")

def get_input():
    N = int(input("Enter the number of games: "))
    return N

def GameOne():
    Initial_Roll = (int(random() * 6) + int(random() * 6)) + 2
    print("Initial Roll:", Initial_Roll)

    if Initial_Roll in {2, 3, 12}:
        print("Player won the roll in 1st roll.")
    elif Initial_Roll in {7, 11}:
        print("Player lost the game in the 1st roll.")
    else:
        print("Player rolls for point.")
        while True:
            Roll = (int(random() * 6) + int(random() * 6)) + 2
            if Roll == 7:
                print("Player lost in the subsequent roll.")
                return False
            elif Roll == Initial_Roll:
                print("Player won in the subsequent roll.")
                return True

def Ngames(N):
    Wins = 0
    Loses = 0
    for _ in range(N):
        if GameOne():
            Wins += 1
        else:
            Loses += 1

    print("Number of Wins:", Wins)
    print("Number of Loses:", Loses)
    print("The win probability is:", Wins / (Wins + Loses))
    print("The win probability is:", Loses / (Wins + Loses))
    return Wins

def main():
    intro()
    Games = get_input()
    Probability = Ngames(Games)

if __name__ == "__main__":
    main()