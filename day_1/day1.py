"""
Find the Elf carrying the most Calories
- Read the file (file pointer)
- Seperate each Elf's food items by a newline
- Add total calories for each elf
- Get the maximum number of calories that represents the Elf carrying the most calories
"""

calory_count = []
count = 0
with open("input.txt",'r') as fp:
    for line in fp:
        if line == '\n':
            calory_count.append(count)
            count = 0
        else:
            count += int(line)
sorted_calory_count = sorted(calory_count,reverse=True)
print(sum(sorted_calory_count[:3]))
