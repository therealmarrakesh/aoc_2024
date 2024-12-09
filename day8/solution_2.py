from collections import defaultdict
from itertools import combinations

antennas = defaultdict(list)
antinodes = set()

with open("input.txt") as f:
    lines = f.readlines()
    rows = len(lines)
    cols = len(lines[0].strip())

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isalnum():
                antennas[char].append((row, col))

print(f"The map is {rows} rows long, and {cols} columns wide")

def is_within(point):
    return 0 <= point[0] < rows and 0 <= point[1] < cols

for entry, positions in antennas.items():
    #print(f"Results for: '{entry}'")
    combos = combinations(positions, 2)
    for combo in combos:
        (row0, col0) = combo[0]
        (row1, col1) = combo[1]

        dr = row1 - row0
        dc = col1 - col0

        antinodes.add(combo[0])
        
        i = 1
        while True:
            antinode_pos = (row0 + i * dr, col0 + i * dc)
            if is_within(antinode_pos):
                antinodes.add(antinode_pos)
            else:
                break
            i += 1

        i = 1
        while True:
            antinode_neg = (row0 - i * dr, col0 - i * dc)
            if is_within(antinode_neg):
                antinodes.add(antinode_neg)
            else:
                break
            i += 1

print(len(antinodes))
