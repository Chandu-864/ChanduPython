from random import random

def simulate_regular_game(prob_A, prob_B):
    score_A = score_B = 0
    while max(score_A, score_B) < 25:
        if random() < prob_A:
            score_A += 1
        else:
            score_B += 1
    return score_A, score_B

def simulate_rally_scoring_game(prob_A, prob_B):
    score_A = score_B = 0
    while max(score_A, score_B) < 25:
        if random() < prob_A:
            score_A += 1
        if random() < prob_B:
            score_B += 1
    return score_A, score_B

def run_simulations(prob_A, prob_B, num_games):
    regular_wins_A = rally_wins_A = 0
    regular_wins_B = rally_wins_B = 0

    for _ in range(num_games):
        reg_score_A, reg_score_B = simulate_regular_game(prob_A, prob_B)
        rally_score_A, rally_score_B = simulate_rally_scoring_game(prob_A, prob_B)

        if reg_score_A > reg_score_B:
            regular_wins_A += 1
        else:
            regular_wins_B += 1

        if rally_score_A > rally_score_B:
            rally_wins_A += 1
        else:
            rally_wins_B += 1

    return (regular_wins_A, regular_wins_B), (rally_wins_A, rally_wins_B)

def main():
    prob_A = float(input("Enter the probability that the better team (Team A) wins a rally: "))
    prob_B = float(input("Enter the probability that the other team (Team B) wins a rally: "))
    num_games = int(input("Enter the number of games to simulate: "))

    regular_results, rally_results = run_simulations(prob_A, prob_B, num_games)

    print("\nRegular Volleyball Games:")
    print(f"Team A wins: {regular_results[0]}, Team B wins: {regular_results[1]}")

    print("\nVolleyball Games with Rally Scoring:")
    print(f"Team A wins: {rally_results[0]}, Team B wins: {rally_results[1]}")

if __name__ == "__main__":
    main()