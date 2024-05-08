import random

def roll():
    min_val = 1
    max_val = 6
    roll_val = random.randint(min_val, max_val)

    return roll_val

while True:
    players = input("Enter number of players (2-4): ")
    if players.isnumeric():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")
    else:
        print("Invalid input!, try again!")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print("\nPlayer number ", i+1," turn has just started!")
        print("Your total score is: ", player_scores[i], "\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll (y)?: ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a ", value)

            print("Your current score is: ", current_score)

        player_scores[i] += current_score
        print("Your total score is: ", player_scores[i])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number ", winning_idx+1, " wins!")