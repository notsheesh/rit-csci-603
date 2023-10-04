import sys 
import os 
import re 

DEBUG = False

def read_file(file_name: str) -> list[list[int]]:
    grid = []
    path = '../data'
    file_path = os.path.join(path, file_name)
    try: 
        with open(file_path) as fn: 
            for line in fn:
                grid_line = [int(x) for x in line.replace('\n', '').split()]
                grid.append(grid_line)
        print("Loaded: {}".format(file_name))
    except IOError:
        print("Couldn't open file {} successfuly".format(file_name))
    return grid

def print_grid(grid: list[list]) -> None: 
    for grid_line in grid: 
        for cell in grid_line:
            print(cell, end=' ')
        print()

def get_grid() -> list[list[int]]: 
    if len(sys.argv) == 2:
        grid = read_file(sys.argv[1])
    elif len(sys.argv) == 3:
        grid = read_file(sys.argv[1])
        try: 
            DEBUG = bool(sys.argv[2])
        except ValueError:
            print("Invalid debug param")
    else:
        print("Enter a valid file name")

    return grid
def is_valid_value(value: int, max_value: int) -> bool:
    if re.fullmatch(r'^[1-9][0-9]*$', value):
        if int(value) <= max_value:
            return True
        else:
            print("Too many lasers to place!")
    else:
        print("Enter a valid positive integer.")

def get_num_lasers(max_num: int) -> int: 
    num_lasers = -1
    while True:
        num_lasers = input("Enter number of lasers: ").strip()
        if is_valid_value(num_lasers, max_num):
            num_lasers = int(num_lasers)            
            break
    return num_lasers

def is_valid_index(grid: list[list[int]], index) -> bool: 
    row_index = index[0]
    col_index = index[1]
    if row_index in range(0, len(grid)):
        if col_index in range(0, len(grid[0])):
            return True
    return False

def is_valid_placement(grid, indices):
    for index in indices:
        if not is_valid_index(grid, index):
            return False
    return True

def get_indices(direction: str, index: tuple[int]):
    row_index = index[0]
    col_index = index[1]

    U = (row_index-1, col_index) # ^ 
    D = (row_index+1, col_index) # v
    L = (row_index, col_index-1) # <
    R = (row_index, col_index+1) # >

    if direction == 'N':
        return (L, U, R) # < ^ >
    if direction == 'S':
        return (L, D, R) # < v > 
    if direction == 'W':
        return (D, L, U) # v < ^
    if direction == 'E':
        return (D, R, U) # v > ^


def is_valid_direction(direction, grid, index):
    indices = get_indices(direction, index)
    if is_valid_placement(grid, indices):
        return True
    return False

# delete comments here
def get_direction_sum(direction, grid: list[list[int]],  index: tuple[int]):
    indices = get_indices(direction, index)
    sum = 0

    # print("index: {} | direction: {}".format(index, direction))
    for idx in indices: 
        # print("Index: {} | Value: {}".format(idx, grid[idx[0]][idx[1]]))
        sum += grid[idx[0]][idx[1]]
    # print("sum: {}".format(sum))
    # print("##################")
    return sum

def make_index_dict(grid, index):
    index_dict = {
            'max_dir': '',
            'max_sum': -1
        }

    for direction in ['N', 'S', 'W', 'E']:
        if is_valid_direction(direction, grid, index):
            direction_sum = get_direction_sum(direction, grid, index)
            if direction_sum > index_dict['max_sum']:
                index_dict['max_dir'] = direction
                index_dict['max_sum'] = direction_sum
    
    return index_dict

def make_grid_dict(grid: list[list[int]]) -> dict:
    grid_dict = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            index = (i, j)
            index_dict = make_index_dict(grid, index)
            if index_dict['max_sum'] != -1:
                grid_dict[index] = index_dict
    return grid_dict

def main():
    grid = get_grid()
    print_grid(grid)
    max_num_lasers = len(grid) * len(grid[0]) - 4
    num_lasers = get_num_lasers(max_num_lasers)
    grid_dict = make_grid_dict(grid)
    # sum_dict = make_sum_dict(grid_dict)

if __name__ == '__main__':
    main()

    





