from random import random

def intro():
    print("")

def inputs():
    prob_A = float(input("Enter the probability that player A wins the serve: "))
    prob_B = float(input("Enter the probability that player B wins the serve: ")) 
    N = int(input("Enter the number of games players will play: "))
    return prob_A, prob_B, N

def gameOne(N, prob_A, prob_B):
    score_A = score_B = 0
    serve = "A"
    while score_A != 15 and score_B != 15:
        if serve == "A":
            if random() < prob_A:
                    score_A += 1
            else:
                    serve = "B"
        else:
            if random() < prob_B:
                    score_B += 1
            else:
                    serve = "A"

    return score_A, score_B

def Ngames(N, prob_A, prob_B):
    wins_A = wins_B = 0
    for i in range(1,N+1):
        score_A, score_B = gameOne(N, prob_A, prob_B)
        if (i % 2 == 0):
            print("For the game",i,"the serve is B")
        else:
            print("For the game",i,"the serve is A")
            if score_A > score_B:
                wins_A += 1
            else:
                wins_B += 1
            return wins_A, wins_B

def main():
    intro()
    prob_A, prob_B, N = inputs()
    wins_A, wins_B = Ngames(N, prob_A, prob_B)
    print("Number of games that Player A won:", wins_A)
    print("Number of games that Player B won:", wins_B)
main()