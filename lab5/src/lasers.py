import sys 
import os 

DEBUG = False

def read_file(file_name: str) -> list[list]:
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
if __name__ == '__main__':
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
    
    print_grid(grid)





