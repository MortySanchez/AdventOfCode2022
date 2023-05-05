"""
    Title:     Advent of Code
    Challenge: Day 1 Part 1 
    Status:    Solved.
    Solution:  205381
"""

elves = []
calories = 0



with open("data.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()

        if stripped_line:
            calories += int(stripped_line)

        if not stripped_line:
            elves.append(calories)
            calories = 0

    if calories:
        elves.append(calories)

elves.sort(reverse=True)
max_calories = int(elves[0]) + int(elves[1]) + int(elves[2])

print(f"Max calories: {max_calories}")


