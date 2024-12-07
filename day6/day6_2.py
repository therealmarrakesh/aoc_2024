import numpy as np

with open("day6_input.txt") as f:
    data = f.read()
    lines = data.splitlines()
    array = np.array([list(line) for line in lines])

revert = array.copy()

class Guard:
    def __init__(self, array):
        self.array = array
        self.position = None
        self.start = None
        self.direction = 'N'
        self.finished = False
        self.visited = set()
        self.looping = False
        self.find_start_pos()
    
    def find_start_pos(self):
        self.position = np.array(np.where(self.array == '^')).flatten()
        self.start = self.position.copy()
    
    def update_positions(self):
        if self.direction == 'N':
            self.ahead = self.position + np.array([-1, 0])
            self.behind = self.position + np.array([1, 0])
        
        elif self.direction == 'E':
            self.ahead = self.position + np.array([0, 1])
            self.behind = self.position + np.array([0, -1])

        elif self.direction == 'S':
            self.ahead = self.position + np.array([1, 0])
            self.behind = self.position + np.array([-1, 0])
        
        elif self.direction == 'W':
            self.ahead = self.position + np.array([0, -1])
            self.behind = self.position + np.array([0, 1])

    def look_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def out_of_bounds(self):
        rows, cols = np.shape(self.array)
        row, col = self.ahead
        return not (0 <= row < rows and 0 <= col < cols)
        
    def move_forward(self):
        if self.out_of_bounds():
            self.finished = True
            return
        
        vector = (tuple(self.position), self.direction)

        if vector in self.visited:
            self.looping = True
            return

        self.visited.add(vector)

        if self.array[tuple(self.ahead)] == '#' or self.array[tuple(self.ahead)] == 'O':
            self.look_right()
            
        else:
            self.position = self.ahead
            self.update_positions()
            
loops = 0

for index, value in np.ndenumerate(array):
    if index == (94, 73):
        continue
    print(f"Simulating obstacle: {index} Loops found: {loops}")
    array = revert.copy()
    array[index] = 'O'
    guard = Guard(array)
    while guard.finished is False and guard.looping is False:
        guard.update_positions()
        guard.move_forward()
    if guard.looping:
        #print("\033[91m\tFound a loop!\033[0m")
        loops += 1
print(loops)
