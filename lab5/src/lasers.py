import sys 
import os 
import re 

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

def get_grid() -> list[list]: 
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

def is_valid_index(grid: list[list], index) -> bool: 
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

def get_indices(direction: str, index: tuple):
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

def get_direction_sum(direction, grid: list[list],  index: tuple):
    indices = get_indices(direction, index)
    sum = 0
    for idx in indices: 
        sum += grid[idx[0]][idx[1]]
    return sum

def get_index_max_sum(grid, index):
    max_sum = -1
    direction = ''
    for direction in ['N', 'S', 'W', 'E']:
        if is_valid_direction(direction, grid, index):
            direction_sum = get_direction_sum(direction, grid, index)
            if direction_sum > max_sum:
                direction = direction
                max_sum = direction_sum
    return max_sum, direction

def make_sums_list(grid: list[list]) -> dict:
    sums_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            index = (i, j)
            max_sum, direction = get_index_max_sum(grid, index)
            if max_sum != -1: 
                sums_list.append([max_sum, index, direction])
    return sums_list

def merge(left_lst: list, right_lst: list):
    merged_lst = []
    left, right = 0, 0
    while left < len(left_lst) and right < len(right_lst):
        if left_lst[left] < right_lst[right]: 
            merged_lst.append(left_lst[left])
            left += 1
        else: 
            merged_lst.append(right_lst[right])
            right += 1

    while left < len(left_lst):
        merged_lst.append(left_lst[left])    
        left += 1
    
    while right < len(right_lst):
        merged_lst.append(right_lst[right])    
        right += 1
    
    return merged_lst

def merge_sort(lst: list):
    if len(lst) < 2: 
        return lst

    left_lst, right_lst = lst[:len(lst)//2], lst[len(lst)//2:]
    return merge(merge_sort(left_lst), merge_sort(right_lst))

def print_optimal_placement(sums_top_k, total_sum_k):
    print("Optimal placement: ")
    for element in sums_top_k:
        print("loc: {}, facing: {}, sum: {}".format(
            element[1], element[2], element[0]
        ))
    print("Total Sum: {}".format(total_sum_k))

def get_triplet(max_sum, sums_list):
    for element in sums_list:
        if max_sum == element[0]:
            return element[0], element[1], element[2]

def get_sums_top_k(sums_sorted, num_lasers, sums_list):
    sums_top_k = []
    for i in range(num_lasers):
        triplet = list(get_triplet(sums_sorted[i], sums_list))
        sums_list.remove(triplet) 
        sums_top_k.append(triplet)
    return sums_top_k

def main():
    grid = get_grid()
    print_grid(grid)
    # Get user input 
    num_lasers = get_num_lasers(len(grid) * len(grid[0]) - 4)
    # Calculate all sums
    sums_list = make_sums_list(grid)
    # Sort sums 
    sums_sorted = merge_sort([element[0] for element in sums_list])[::-1]
    # Get top k 
    sums_top_k = get_sums_top_k(sums_sorted, num_lasers, sums_list)
    total_sum_k = sum(sums_sorted[:num_lasers])
    print_optimal_placement(sums_top_k, total_sum_k)

if __name__ == '__main__':
    main()

    





