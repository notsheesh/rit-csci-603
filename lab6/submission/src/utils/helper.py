import re 
from os import path, listdir
from sys import argv, exit

def parse_args(args):
    """
    Parses command-line arguments and checks if they meet specific criteria.

    :param args: List of command-line arguments.
    :return: The filename derived from the command-line argument.
    """
    if len(args) != 2 or not re.fullmatch(r'data_\d+', args[1]):
        print("Usage: python3 airit.py {filename}")
        exit(-1)

    file_name = args[1] + ".txt"

    if not file_name in listdir(path.join('..', 'data')):
        print("File not found: {}".format(args[1]))
        exit(-1)
    
    return file_name

def _sanitize(element):
    """
    Sanitizes a data element by splitting and converting it into a structured dictionary.

    :param element: A line from the data file.
    :return: A dictionary containing passenger details.
    """
    has_carry_on = True if element.strip().split(',')[2] == "True" else False
    return {
        'name': element.strip().split(',')[0],
        'ticket_number': int(element.strip().split(',')[1]),
        'has_carry_on': has_carry_on
    }

def get_data(file_name):
    """
    Reads and structures passenger data from a file.

    :param file_name: Name of the file to be read
    :return: A list of dictionaries containing passenger details.
    """
    try:
        with open(path.join('..', 'data', file_name), 'r') as file:
            print("Reading passenger data from {}".format(file_name))
            _data = [_sanitize(line) for line in file.readlines()]
    except OSError:
        print("Could not open/read file:".format())
        exit()
    return _data

def get_capacity(var_name):
    """
    Prompts the user to input a maximum capacity for a variable and validates the input.

    :param var_name: The name of the variable for which capacity is being set.
    :return: The validated maximum capacity as an integer.
    """
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