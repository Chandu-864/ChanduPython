from random import random

def intro():
    print("Welcome to the racquet game simulator!")

def inputs():
    prob_A = float(input("Enter the probability that player A wins the serve: "))
    prob_B = float(input("Enter the probability that player B wins the serve: "))
    N = int(input("Enter the number of games players will play: "))
    return prob_A, prob_B, N

def gameOne(prob_A, prob_B):
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
    
    if score_A == 15:
        print("Player A has won the game")
    else:
        print("Player B has won the game")

    return score_A, score_B

def Ngames(N, prob_A, prob_B):
    wins_A = wins_B = player1 = player2 = 0
    
    for i in range(1, N+1):
        if i % 2 == 1:
            serve = "A"
        else:
            serve = "B"
        
        print("Now, for game", i, ", the first serve starts with player:", serve)
        score_A, score_B = gameOne(prob_A, prob_B)
        
        if score_A == 0:
            print("Player B has shutout game", i)
            player1 += 1
        elif score_B == 0:
            print("Player A has shutout game", i)
            player2 += 1

        if score_A > score_B:
            wins_A += 1
        else:
            wins_B += 1

    return wins_A, wins_B, player1, player2

def main():
    intro()
    prob_A, prob_B, N = inputs()
    wins_A, wins_B, player1, player2 = Ngames(N, prob_A, prob_B)
    print("________________________________________________________________________________________________")
    print("Number of games that Player A won:", wins_A)
    print("Number of games that Player B won:", wins_B)
    print("Number of shutout game that Player A has:", player2)
    print("Number of shutout game that Player B has:", player1)
    print("Percentage of games that Player A won:", ((wins_A/N)*100),"%")
    print("Percentage of games that Player B won:", ((wins_B/N)*100),"%")
    if player1 == 0 and player2 == 0:
        print("Neither player has won any shutout games.")
    else:    
        if wins_A >= 0:
            if player2 > 0:
                print("percentage of wins that are shutouts Player A has won:", ((player2/wins_A)*100),"%")
            else:
                print("Player A has no shutout games")

        if wins_B >= 0:        
            if player1 > 0:
                print("percentage of wins that are shutouts Player B has won:", ((player1/wins_B)*100),"%")
            else:
                print("Player B has no shutout games")
    print("________________________________________________________________________________________________")
    
    
main()