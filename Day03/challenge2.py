"""
    Title:     Advent of Code
    Challenge: Day 3 Part 2
    Status:    Solved.
    Solution:  2697
"""

import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def get_batch(rucksack1, rucksack2, rucksack3):
    for item_type in rucksack1:
        if item_type in rucksack2 and item_type in rucksack3:
            return item_type

rucksacks = 0
group = []
group_number = 0
sum_of_priorities = 0

with open("data.txt", "r") as file:
    for line in file:
        rucksack = line.strip()
        
        # add rucksack to group 
        group.append(rucksack)

        # increase rucksack counter
        rucksacks += 1

        # check group size to call function for complete group
        if rucksacks == 3:
            group_number += 1
            batch = get_batch(group[0], group[1], group[2])
            value = letters.index(batch) + 1

            # set priorieties
            sum_of_priorities += value

            # output
            print("_____________________\n")
            print(f"Group {group_number}")
            print(f"Batch {batch}")
            print(f"Value {value}")


            
            # reset group
            rucksacks = 0
            group.clear()

print("==========")
print(f"Sum: {sum_of_priorities}")
print("==========")