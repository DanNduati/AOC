"""
Camp Cleanup
------------
1. Loop through all section assignment pairs
    -> Split on the comma to get each
    -> use the range function to create a list of each
    -> use a set method(look this up) to potentially get the "full contained in another pair"
2. Find number of assignment pairs fully contained in others
"""


def check_contained(a, b: list[str]) -> bool:
    range_a = list(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    range_b = list(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if set(range_a).issubset(set(range_b)) or set(range_b).issubset(set(range_a)):
        return True
    return False

count = 0
with open("input.txt", "r") as fp:
    for line in fp:
        pair = line.strip()
        a, b = pair.split(",")
        if (check_contained(a, b)):
            count+=1
print(count)
