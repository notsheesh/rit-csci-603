"""
Lab 5: Lasers

A Python script for optimizing the placement of lasers on a grid, maximizing the
sum of the beams.

It reads a grid from a file, calculates all possible laser placements, and finds
the optimal placements.

author: Shreesh Tripathi, st4083
"""
import sys 
import os 
import re 
from collections import OrderedDict

def read_file(file_name: str) -> OrderedDict:
    """
    Reads a file containing a grid of integers and returns it as OrderedDict.

    :param file_name: The name of the file to read.

    :return: An OrderedDict representing the grid.
    """
    grid_dict = OrderedDict()
    path = '../data'
    file_path = os.path.join(path, file_name)
    try: 
        with open(file_path) as fn: 
            count = 0 
            for line in fn:
                grid_line = [int(x) for x in line.replace('\n', '').split()]
                grid_dict[count] = grid_line
                count += 1
        print("Loaded: {}".format(file_name))
        return grid_dict
    
    except IOError:
        return grid_dict

def print_grid(grid: list[list]) -> None: 
    """
    Prints the grid represented as a list of lists.

    :param grid: The grid to be printed.
    """
    for grid_line in grid: 
        for cell in grid_line:
            print(cell, end=' ')
        print()

def parse_dict(grid_dict: OrderedDict) -> list:
    """
    Converts a grid dictionary to a list of lists.

    :param grid_dict: The grid represented as an ordered dictionary.

    :return: A list of lists representing the grid.
    """
    grid = []
    num_rows = len(grid_dict)
    for i in range(num_rows):
        grid.append(grid_dict[i])
    return grid

def get_grid() -> list[list]: 
    """
    Reads a grid from a file specified in the command-line arguments or user 
    input.

    :return: The grid as a list of lists.
    """
    grid = []
    if len(sys.argv) == 2:
        grid_dict = read_file(sys.argv[1])
        grid = parse_dict(grid_dict)

    if len(grid) > 0:
        return grid
    else: 
        print("Usage: python3 lasers.py filename")
        sys.exit(-1)

def is_valid_value(value: int, max_value: int) -> bool:
    """
    Checks if a value is a valid positive integer within a given range.

    :param value: The value to be checked.
    :param max_value: The maximum allowed value.

    :return: True if the value is valid, False otherwise.
    """
    if re.fullmatch(r'^[0-9]*$', value):
        if int(value) <= max_value:
            return True
        else:
            print("Too many lasers to place!")
            return False
    else:
        print("Enter a valid positive integer.")

def get_num_lasers(num_cells: int) -> int: 
    """
    Prompts the user to enter the number of lasers to be placed.

    :param num_cells: The total number of cells available.

    :return: The number of lasers as an integer.
    """
    num_max = num_cells - 4
    num_lasers = -1
    while True:
        num_lasers = input("Enter number of lasers: ").strip()
        if is_valid_value(num_lasers, num_max):
            num_lasers = int(num_lasers)            
            break
        else: # Too many lasers to place
            sys.exit(-1)
    return num_lasers

def is_valid_beam_position(grid: list[list], index) -> bool: 
    """
    Checks if a given index is a valid position within the grid.

    :param grid: The grid represented as a list of lists.
    :param index: The index to be checked.

    :return: True if the index is a valid position, False otherwise.
    """
    row_index = index[0]
    col_index = index[1]
    if row_index in range(0, len(grid)):
        if col_index in range(0, len(grid[0])):
            return True
    return False

def is_valid_laser_placement(grid: list[list], indices: tuple[tuple]):
    """
    Checks if a laser placement, consisting of multiple beam positions, is valid

    :param grid: The grid represented as a list of lists.
    :param indices: A tuple of indices representing the positions of the beams.

    :return: True if the laser placement is valid, False otherwise.
    """
    for index in indices:
        if not is_valid_beam_position(grid, index):
            return False
    return True

def get_indices(direction: str, index: tuple) -> tuple: 
    """
    Calculates the indices of beams in a laser placement based on a given 
    direction.

    :param direction: The direction of the laser ('N', 'S', 'W', or 'E').
    :param index: The index of the initial beam.

    :return: A tuple of indices representing beam positions in the given 
    direction.
    """
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


def is_valid_laser_direction(direction: str, grid: list[list], index: tuple):
    """
    Checks if a laser placement in a given direction is valid on the grid.

    :param direction: The direction of the laser ('N', 'S', 'W', or 'E').
    :param grid: The grid represented as a list of lists.
    :param index: The index of the initial beam.

    :return: True if the laser placement in the given direction is valid, False 
    otherwise.
    """
    indices = get_indices(direction, index)
    if is_valid_laser_placement(grid, indices):
        return True
    return False

def get_direction_sum(direction, grid: list[list],  index: tuple):
    """
    Calculates the sum of beam values in a specific direction from a given index

    :param direction: The direction of the laser ('N', 'S', 'W', or 'E').
    :param grid: The grid represented as a list of lists.
    :param index: The index of the initial beam.

    :return: The sum of beam values in the given direction.
    """
    indices = get_indices(direction, index)
    sum = 0
    for idx in indices: 
        sum += grid[idx[0]][idx[1]]
    return sum

def get_index_max_sum(grid: list[list], index: tuple):
    """
    Finds the maximum sum and direction from a given index.

    :param grid: The grid represented as a list of lists.
    :param index: The index of the initial beam.

    :return: A tuple containing the maximum sum and corresponding direction.
    """
    max_sum = -1
    max_direction = ''
    for direction in ['N', 'S', 'W', 'E']:
        if is_valid_laser_direction(direction, grid, index):
            direction_sum = get_direction_sum(direction, grid, index)
            if direction_sum > max_sum:
                max_direction = direction
                max_sum = direction_sum
    return max_sum, max_direction

def make_sums_list(grid: list[list]) -> dict:
    """
    Generates a list of sums for all possible laser placements on the grid.

    :param grid: The grid represented as a list of lists.

    :return: A list of sums, each sum associated with its position and direction
    """
    sums_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            index = (i, j)
            max_sum, direction = get_index_max_sum(grid, index)
            if max_sum != -1: 
                sums_list.append([max_sum, index, direction])
    return sums_list

def merge(left_lst: list, right_lst: list):
    """
    Merges two sorted lists into a single sorted list.

    :param left_lst: The left sorted list.
    :param right_lst: The right sorted list.

    :return: A merged sorted list.
    """
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
    """
    Sorts a list using the merge sort algorithm.

    :param lst: The list to be sorted.

    :return: A sorted list.
    """
    if len(lst) < 2: 
        return lst

    left_lst, right_lst = lst[:len(lst)//2], lst[len(lst)//2:]
    return merge(merge_sort(left_lst), merge_sort(right_lst))

def print_optimal_placement(sums_top_k: list, total_sum_k: int) -> None:
    """
    Prints the optimal placement of lasers and their total sum.

    :param sums_top_k: A list of optimal laser placements.
    :param total_sum_k: The total sum of laser placements.
    """
    print("Optimal placement: ")
    for element in sums_top_k:
        print("loc: {}, facing: {}, sum: {}".format(
            element[1], element[2], element[0]
        ))
    print("Total Sum: {}".format(total_sum_k))

def get_triplet(max_sum: int, sums_list: list) -> tuple:
    """
    Retrieves a triplet from the list based on its maximum sum.

    :param max_sum: The maximum sum to search for.
    :param sums_list: A list of sums with associated positions and directions.

    :return: A triplet containing the maximum sum, position, and direction.
    """
    for element in sums_list:
        if max_sum == element[0]:
            return element[0], element[1], element[2]

def get_sums_top_k(sums_sorted: list, num_lasers: int, sums_list: list) -> None:
    """
    Retrieves the top-k laser placements and their total sum.

    :param sums_sorted: A sorted list of sums.
    :param num_lasers: The number of lasers to place.
    :param sums_list: A list of sums with associated positions and directions.

    :return: A list of top-k laser placements.
    """
    sums_top_k = []
    for i in range(num_lasers):
        triplet = list(get_triplet(sums_sorted[i], sums_list))
        sums_list.remove(triplet) 
        sums_top_k.append(triplet)
    return sums_top_k


def main():
    """
    Driver function for processing the laser placement on the grid, sorting and
    finding optimal placements.
    """
    grid = get_grid()

    # Stdout
    print_grid(grid)

    # Get user input 
    num_lasers = get_num_lasers(len(grid) * len(grid[0]))

    # Calculate all sums
    sums_list = make_sums_list(grid)

    # Sort sums 
    sums_sorted = merge_sort([element[0] for element in sums_list])[::-1]

    # Get top k 
    sums_top_k = get_sums_top_k(sums_sorted, num_lasers, sums_list)
    total_sum_k = sum(sums_sorted[:num_lasers])

    # Stdout Answer
    print_optimal_placement(sums_top_k, total_sum_k)

if __name__ == '__main__':
    main()