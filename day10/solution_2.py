map_data = []
all_paths = 0

with open("input.txt") as f:
    for line in f:
        map_data.append([int(char) for char in line.strip()])

for line in map_data:
    print(line)

width = len(map_data[0])
length = len(map_data)

class Node:
    def __init__(self, row, col, elevation):
        self.r = row
        self.c = col
        self.e = elevation
        self.ahead = []
        self.behind = None

    def get_neighbors(self, map_data, width, length):
        # Check up
        if self.r > 0 and map_data[self.r - 1][self.c] - self.e == 1:
            neighbor = Node(self.r - 1, self.c, map_data[self.r - 1][self.c])
            neighbor.behind = self
            self.ahead.append(neighbor)

        # Check down
        if self.r < length - 1 and map_data[self.r + 1][self.c] - self.e == 1:
            neighbor = Node(self.r + 1, self.c, map_data[self.r + 1][self.c])
            neighbor.behind = self
            self.ahead.append(neighbor)

        # Check left
        if self.c > 0 and map_data[self.r][self.c - 1] - self.e == 1:
            neighbor = Node(self.r, self.c - 1, map_data[self.r][self.c - 1])
            neighbor.behind = self
            self.ahead.append(neighbor)

        # Check right
        if self.c < width - 1 and map_data[self.r][self.c + 1] - self.e == 1:
            neighbor = Node(self.r, self.c + 1, map_data[self.r][self.c + 1])
            neighbor.behind = self
            self.ahead.append(neighbor)



def find_paths(node, map_data, width, length, current_path):
    global all_paths
    #print(f"Checking trailhead at {node.r}, {node.c}")

    current_path.append(node)

    if node.e == 9:
        print("Path found!")
        for n in current_path:
            print(f"({n.r}, {n.c}) -> ", end="")
        print("End")
        all_paths += 1
        current_path.pop()
        return

    node.get_neighbors(map_data, width, length)

    for neighbor in node.ahead:
        if neighbor not in current_path:
            find_paths(neighbor, map_data, width, length, current_path)
    
    current_path.pop()
    




for row, line in enumerate(map_data):
    for col, height in enumerate(line):
        if height == 0:
            trailhead = Node(row, col, height)
            current_path = []
            find_paths(trailhead, map_data, width, length, current_path)


print(all_paths)
