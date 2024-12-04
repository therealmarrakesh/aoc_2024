import numpy as np
import re

with open("day4_input.txt") as f:
    data = re.sub(r'\s+', '', ''.join(f.read()))
    array = np.array(list(data)).reshape(140, 140)

total = 0

for i, row in enumerate(array[1:-1], start=1):
    for j, char in enumerate(row[1:-1], start=1):
        if char == 'A':
            neighbors = [
                array[i-1, j-1],
                array[i+1, j-1],
                array[i-1, j+1],
                array[i+1, j+1]
                ]
            neighbor_str = ''.join(neighbors)
            if neighbor_str.count("M") == 2 and neighbor_str.count("S") == 2:
                if neighbor_str[0] != neighbor_str[3]:
                    total += 1

print(total)
