"""
    Title:     Advent of Code
    Challenge: Day 3 Part 1
    Status:    To be solved.
    Solution:  
"""

import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

sum_of_priorities = 0
rucksack_counter = 0

print("==================================")
    
with open("data.txt", "r") as file:
    for line in file:
        rucksack = line.strip()

        rucksack_counter += 1

        # split rucksack into two compartements
        middle_index = len(rucksack) // 2
        comp1, comp2 = rucksack[:middle_index], rucksack[middle_index:]

        print("Rucksack: " + str(rucksack_counter))
        print("Comp1: " + comp1)
        print("Comp2: " + comp2)

        for item_type in comp1:
            if item_type in comp2:
                sum_of_priorities += letters.index(item_type) + 1
                break
        print("==================================")

print("Sum of priorities: " + str(sum_of_priorities))