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


def make_sum_dict1(grid_dict: dict) -> dict:
    sum_dict = {}
    for key in grid_dict:
        index = key
        max_dir = grid_dict[index]['max_dir']
        max_sum = grid_dict[index]['max_sum']
        sum_dict[max_sum] = {
            'direction': max_dir,
            'index': index
        }        

    return sum_dict