"""
Rucksack Reorganization
-----------------------
Part one

1. Loop through each rucksack and add the items that appear on both string slices to a list
2. Calculate the cumulative priority of the items that are on the above list

Part two

1. Loop through group of three rucksacks(group) checking for an item type that appears im all three
2. Calculate cumulative priority as above
"""


def calculate_priority(char: str) -> int:
    if char.islower():
        return int(ord(char) - ord("a")) + 1
    return int(ord(char) - ord("A")) + 27


def calc_priority_rucksack() -> int:
    priority = 0
    with open("input.txt", "r") as fp:
        for line in fp:
            line = line.strip()
            first_compartment = line[: int(len(line) / 2)]
            second_compartment = line[int(len(line) / 2) :]
            for char in first_compartment:
                if second_compartment.count(char) > 0:
                    priority += calculate_priority(char)
                    break  # Expecting only one misplaced item
    return priority


def find_badge_type(ls: list[str]) -> str:
    common = set.intersection(*map(set, ls))
    return str(list(common)[0])


def calc_priority_group() -> int:
    group = []
    priority = 0
    with open("input.txt", "r") as fp:
        priority = count = 0
        for line in fp:
            line = line.strip()
            group.append(line)
            count += 1
            if count % 3 == 0:
                # Find the badge type for the group
                badge_type = find_badge_type(group)
                # Calculate priority
                priority += calculate_priority(badge_type)
                group.clear()
    return priority


def main():
    print(calc_priority_rucksack())
    print(calc_priority_group())


if __name__ == "__main__":
    main()
