columnA = []
columnB = []
total = 0

with open("day1_input.txt") as f:
    for line in f:
        valueA, valueB = line.split()
        columnA.append(int(valueA))
        columnB.append(int(valueB))

columnA.sort()
columnB.sort()

for a in columnA:
    count = columnB.count(a)
    total += a * count

print(total)
