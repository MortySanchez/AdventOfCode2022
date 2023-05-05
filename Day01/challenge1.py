"""
    Title:     Advent of Code
    Challenge: Day 1 Part 1 
    Status:    To be solved.
    Solution:  
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

print(f"Number of elves: {len(elves)}")
print("Calories:")

index = 0
pos = 1
for elve in elves:
    print("Pos " + str(pos) + ".)" + " " + str(elve))
    index += 1
    pos += 1

elves.sort()
most_calories = elves[-1]
print(f"Most calories: {most_calories}")

