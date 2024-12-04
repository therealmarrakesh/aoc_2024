import numpy as np
import re

pattern = r"(?=(XMAS|SAMX))"
total = 0

with open("day4_input.txt") as f:
    data = re.sub(r'\s+', '', ''.join(f.read()))
    array = np.array(list(data)).reshape(140, 140)

rows, cols = array.shape

def get_horizontal(array):
    global total
    for i in range(rows):
        row_str = ''.join(array[i])
        total += len(re.findall(pattern, row_str))
        #print("Horizontal:", len(re.findall(pattern, row_str)))

def get_vertical(array):
    global total
    for i in range(cols):
        cols_str = ''.join(array[:, i])
        total += len(re.findall(pattern, cols_str))
        #print("Vertical:", len(re.findall(pattern, cols_str)))

def get_diagonals(array):
    global total

    # get the primary diagonals from first row
    for i in range(cols):
        diagonal_str = ''.join(array.diagonal(offset=i))
        total += len(re.findall(pattern, diagonal_str))
        #print("DiagonalP1:", len(re.findall(pattern, diagonal_str)))
    
    # get the primary diagonals from first column
    for i in range(1, rows):
        diagonal_str = ''.join(array.diagonal(offset=-i))
        total += len(re.findall(pattern, diagonal_str))
        #print("DiagonalP2:", len(re.findall(pattern, diagonal_str)))

    flipped_array = np.fliplr(array)
    frows, fcols = flipped_array.shape

    # get secondary diagonals from first row
    for i in range(fcols):
        diagonal_str = ''.join(flipped_array.diagonal(offset=i))
        total += len(re.findall(pattern, diagonal_str))
        #print("DiagonalS1:", len(re.findall(pattern, diagonal_str)))
        

    # get secondary diagonals from last column
    for i in range(1, frows):
        diagonal_str = ''.join(flipped_array.diagonal(offset=-i))
        total += len(re.findall(pattern, diagonal_str))
        #print("DiagonalS2:", len(re.findall(pattern, diagonal_str)))

get_horizontal(array)
get_vertical(array)
get_diagonals(array)
print(total)
