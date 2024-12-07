import numpy as np

with open("day6_input.txt") as f:
    data = f.read()
    lines = data.splitlines()
    array = np.array([list(line) for line in lines])

class Guard:
    def __init__(self, array):
        self.array = array
        self.position = None
        self.direction = 'N'
        self.finished = False
        self.find_start_pos()
    
    def find_start_pos(self):
        self.position = np.array(np.where(self.array == '^')).flatten()
        print("The level is size:", np.shape(self.array))
        print("Starting position:", self.position)
    
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
            array[tuple(self.position)] = 'X'
            self.finished = True

        elif self.array[tuple(self.ahead)] == '#':
            #print("Encountered obstacle!")
            self.look_right()
            #print("Now direction is:", self.direction)
        
        else:
            self.position = self.ahead
            self.update_positions()
            #print("Moving forward!")
            self.array[tuple(self.behind)] = 'X'

guard = Guard(array)
while guard.finished is False:
    guard.update_positions()
    guard.move_forward()
    #print(guard.array)
print("Finished!")
print(guard.array)
steps = np.count_nonzero(array == 'X')
print("Total number of steps taken:", steps)
