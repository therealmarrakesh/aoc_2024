files = []
file_num = 0
total = 0

with open("input.txt") as f:
    file = list(f.read().strip())

for index, char in enumerate(file):
    if index % 2 == 0:
        for i in range(int(char)):
            files.append(file_num)
        file_num += 1

    else:
        for i in range(int(char)):
            files.append(".")

#print(files)


def compress(files):
    i = len(files) - 1
    checked_values = set()

    while i > 0:
        if files[i] != '.':
            if files[i] in checked_values:
                i -= 1
                continue
            file = [i]
            j = i - 1
            while j > 0 and files[j] == files[i]:
                file.append(j)
                j -= 1
            i = j

            print("Checking:", files[file[0]])
            checked_values.add(files[file[0]])
            print(file)

            gap_found = False
            for gap in find_gaps(files):
                if gap[0] < file[0] and len(file) <= gap[1]:
                    print("Found a gap!")
                    k = 0
                    for entry in file:
                        files[entry], files[gap[0] + k] = files[gap[0] + k], files[entry]
                        k += 1
                    gap_found = True
                    break
            
            if not gap_found:
                print(f"No gap found for {files[file[0]]}")

            #print(files)

        else:
            i -= 1
    return



def find_gaps(files):
    gap_list = []
    i = 0
    while i < len(files):
        if files[i] == ".":
            start = i
            j = i + 1
            while j < len(files) and files[j] == ".":
                j += 1
            end = j - 1
            gap_length = end - start + 1
            gap_list.append((start, gap_length))
            i = j
        else:
            i += 1
    return gap_list




compress(files)


for index, char in enumerate(files):
    if isinstance(char, int):
        total += char * index
    else:
        continue

#print(files)
print(total)
