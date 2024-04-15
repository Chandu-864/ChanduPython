from random import random
def intro():
    print("This is a simulation for 'Table Tennis game'")
def inputs():
    prob_A = float(input("Enter the probability that the player A wins the serve: "))
    prob_B = float(input("Enter the probability that the player B wins the serve: ")) 
    N = int(input("Enter the number of games players will play: "))
    return prob_A, prob_B, N
def gameone(N,prob_A, prob_B):
    score_A = score_B = 0
    serve = "A"
    while True:
        if N % 2 == 0:
            serve = "B"
        else:
            serve = "A"
            
        if (score_A + score_B) % 2 == 0:
        
            
                
        if serve == "A":
            if random() < prob_A:
                score_A = score_A + 1
            else:
                score_B = score_B + 1
        elif serve == "B":
            if random() < prob_B:
                score_B = score_B + 1
            else:
                score_A = score_A + 1
        if (score_A >= 11) and (score_A > (score_B + 1)):
            print("Player 'A' is winner")
            break
        else:
            if (score_B >= 11) and (score_B > (score_A + 1)):
                print("Player 'B' is winner")
                break
    print("The serve for the game",N,"is",serve)
    print("The scores are ->","A:",score_A,"B:",score_B)
    return score_A, score_B

def Ngames(N, prob_A, prob_B):
    wins_A= wins_B = 0
    for i in range(N):
        score_A, score_B = gameone(N,prob_A, prob_B)
        if score_A > score_B:
            wins_A = wins_A + 1
        else:
            wins_B = wins_B + 1
    return wins_A, wins_B
def main():
    intro()
    prob_A, prob_B, N = inputs()
    wins_A, wins_B = Ngames(N, prob_A, prob_B)
    print("Number of games that Player A won: ", wins_A)
    print("Number of games that Player B won: ", wins_B)
main()

