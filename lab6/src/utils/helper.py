import re 
from os import path, listdir
from sys import argv, exit

def _parse_args(args):
    
    if len(args) != 2 or not re.fullmatch(r'data_\d+', args[1]):
        print("Usage: python3 airit.py {filename}")
        exit(-1)

    _file_name = args[1] + ".txt"
    _file_dir_path = path.join('..', 'data')

    if not _file_name in listdir(_file_dir_path):
        print("File not found: {}".format(args[1]))
        exit(-1)
    
    return _file_name

def _sanitize(element):
    has_carry_on = True if element.strip().split(',')[2] == "True" else False
    return {
        'name': element.strip().split(',')[0],
        'ticket_number': int(element.strip().split(',')[1]),
        'has_carry_on': has_carry_on
    }

def get_data(args):
    _file_name = _parse_args(args)
    _file_path = path.join('..', 'data', _file_name)
    try:
        with open(_file_path, 'r') as file:
            print("Reading passenger data from {}".format(_file_name))
            _data = [_sanitize(line) for line in file.readlines()]
    except OSError:
        print("Could not open/read file:".format())
        exit()
    return _data

def get_capacity(var_name):
    while True: 
        max_val = input("{} capacity: ".format(var_name))
        if re.fullmatch(r'[0-9]*', max_val) and int(max_val) > 0:
            return int(max_val)
        else:
            print("Invalid input! Please enter a valid positive integer")
            continue

def main():
    pass

if __name__ == '__main__':
    main()