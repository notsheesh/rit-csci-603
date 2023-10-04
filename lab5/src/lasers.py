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

def main():
    grid = get_grid()
    print_grid(grid)
    max_num_lasers = len(grid) * len(grid[0]) - 4
    num_lasers = get_num_lasers(max_num_lasers)

if __name__ == '__main__':
    main()

    





