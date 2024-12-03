import re

total = 0

with open("day3_input.txt") as f:
    for line in f:
        search = re.findall(r'mul\(\d*,\d*\)', line)
        for item in search:
            nums = re.sub(r"[mul()]", "", item)
            m, n = map(int, nums.split(","))
            total += m * n

print(total)
