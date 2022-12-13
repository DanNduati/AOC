"""
Rucksack Reorganization
-----------------------
Part one

1. Loop through each rucksack and add the items that appear on both string slices to a list
2. Calculate the cumulative priority of the items that are on the above list
"""


def calculate_priority(char: str) -> int:
    if char.islower():
        return int(ord(char) - ord("a")) + 1
    return int(ord(char) - ord("A")) + 27


misplaced = []
with open("input.txt", "r") as fp:
    priority = 0
    for line in fp:
        line = line.strip()
        first_compartment = line[: int(len(line) / 2)]
        second_compartment = line[int(len(line) / 2) :]
        for char in first_compartment:
            if second_compartment.count(char) > 0:
                priority += calculate_priority(char)
                break  # Expecting only one misplaced item
    print(priority)
