rules = []
updates = []
total = 0

with open("day5_input1.txt") as f1:
    for line in f1:
        rule = line.strip().split("|")
        rules.append(rule)

with open("day5_input2.txt") as f2:
    for line in f2:
        update = line.strip().split(",")
        updates.append(update)

for update in updates:

    violation = False
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                violation = True
                break

    if not violation:
        total += int(update[int(len(update) / 2)])

print(total)
