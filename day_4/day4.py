"""
Camp Cleanup
------------
1. Loop through all section assignment pairs
    -> Split on the comma to get each
    -> use the range function to create a list of each
    -> use a set method(look this up) to potentially get the "full contained in another pair"
2. Find number of assignment pairs fully contained in others
"""


def check_subset(a, b: list[str]) -> bool:
    range_a = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    range_b = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if range_a.issubset(range_b) or range_b.issubset(range_a):
        return True
    return False


def check_overlap(a, b: list[str]) -> bool:
    range_a = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    range_b = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if range_a.intersection(range_b):
        return True
    return False


subset_count = overlap_count = 0
with open("input.txt", "r") as fp:
    for line in fp:
        pair = line.strip()
        a, b = pair.split(",")
        if check_subset(a, b):
            subset_count += 1
        if check_overlap(a, b):
            overlap_count += 1
print(
    f"Assignment pairs that full contain the other {subset_count}\nAssignment pairs with overlaping ranges {overlap_count}"
)
