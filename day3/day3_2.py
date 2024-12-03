import re

total = 0
mul = r"mul\(\d*,\d*\)"
do = r"do()"
dont = r"don\'t()"
pattern = r"mul\(\d*,\d*\)|don\'t()|do()"
enabled = True


with open("day3_input.txt") as f:
    content = f.read()

for match in re.finditer(pattern, content):
    match_str = match.group()
    print(match_str)
    if re.match(mul, match_str):
        if enabled:
            nums = re.sub(r"[mul()]", "", match_str)
            m, n = map(int, nums.split(","))
            total += m * n
    elif re.match(dont, match_str):
        enabled = False
    else:
        enabled = True

print(total)
