"""
    Title:     Advent of Code
    Challenge: Day 2 Part 1 
    Status:    Solved.
    Solution:  10994
"""

# Dict to translate opponents hand
opponent = { 
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors"
}

    
# Dict to translate players hand    
player = {
    "X":"Rock",
    "Y":"Paper",
    "Z":"Scissors"
}

    
# Dict to evaluate points for hand and result
points = {
    "Rock":1,
    "Paper":2,
    "Scissors":3,
    "Win":6,
    "Loose":0,
    "Draw":3
}


# Total score for solution
total_score = 0


# Get result, if player wins, looses or has a draw with opponent
def get_result(opponent_hand, player_hand):
    if opponent[opponent_hand] == player[player_hand]:
        return "Draw"
    elif  (opponent[opponent_hand] == "Rock" and player[player_hand] == "Paper") or (opponent[opponent_hand] == "Paper" and player[player_hand] == "Scissors") or (opponent[opponent_hand] == "Scissors" and player[player_hand] == "Rock"):
        return "Win"
    else:
        return "Loose"
        

# Evaluate the round score for the player
def get_score(result, player_hand):
    return points[result] + points[player[player_hand]]
    

# Main program

index = 0
round = 1
with open("data.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()
        split_line = stripped_line.split(" ")

        print(f"Round: {round}")
        round_result = get_result(split_line[0], split_line[1])
        round_score = get_score(round_result, split_line[1])

        print(f"Result: {round_result}")
        print(f"Score: {round_score}")

        total_score += round_score
        round += 1
        print("==================")


print("Game over!")
print(f"Total score: {total_score}")
print("==================")
print("==================")
