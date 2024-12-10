uncompressed = []
file_num = 0
total = 0

with open("input.txt") as f:
    file = list(f.read().strip())

for index, char in enumerate(file):
    if index % 2 == 0:
        for i in range(int(char)):
            uncompressed.append(file_num)
        file_num += 1

    else:
        for i in range(int(char)):
            uncompressed.append(".")

print(uncompressed)


def compress(uncompressed):
    last = len(uncompressed) - 1
    
    for index, char in enumerate(uncompressed):
        if index >= last:
            break
        if char == '.':
            while uncompressed[last] == '.' and index < last:
                last -= 1
            uncompressed[index], uncompressed[last] = uncompressed[last], uncompressed[index]

compress(uncompressed)


for index, char in enumerate(uncompressed):
    if isinstance(char, int):
        total += char * index
    else:
        continue

print(uncompressed)
print(total)
