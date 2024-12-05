rules = []
updates = []
incorrect = []
corrected = []

with open("day5_input1.txt") as f1:
    for line in f1:
        rule = line.strip().split("|")
        rules.append(rule)

with open("day5_input2.txt") as f2:
    for line in f2:
        update = line.strip().split(",")
        updates.append(update)

def is_correct(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

for update in updates:

    violation = False
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                violation = True
                break

    if violation:
        incorrect.append(update)

print("Incorrect:", len(incorrect))

for update in incorrect:
    while is_correct(update) is False:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    a = update.index(rule[0])
                    b = update.index(rule[1])
                    update[a], update[b] = update[b], update[a]
    print(update)
    corrected.append(update)

print("Corrected:", len(corrected))

total = 0

for correct in corrected:
    total += int(correct[int(len(correct) / 2)])

print("Total:", total)
