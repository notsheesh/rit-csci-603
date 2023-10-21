
import re 
from os import path, listdir
from sys import argv, exit
from _queue import Queue

def get_file_name() -> str: 
    
    if len(argv) != 2 or not _is_proper_file_name(argv[1]):
        print("Usage: python3 airit.py {filename}")
        exit(-1)

    if not _is_file_path_exist(path.join('..', 'data'), argv[1]):
        print("File not found: {}".format(argv[1]))
        exit(-1)
    
    return argv[1] + ".txt"

def _is_proper_file_name(_file_name: str) -> bool: 
    _proper_file_regex = r'data_\d+'
    if re.fullmatch(_proper_file_regex, _file_name):
        return True
    return False

def _is_file_path_exist(_file_dir_path: str, _file_name: str) -> bool: 
    return _file_name + '.txt' in listdir(_file_dir_path)

def get_data() -> list[list[str]]: 
    _file_name = get_file_name()
    _file_path = path.join('..', 'data', _file_name)
    try:
        with open(_file_path, 'r') as file:
            data = [line.strip().split(',') for line in file.readlines()]
    except OSError:
        print("Could not open/read file:".format())
        exit()
    return data

def test() -> None:
    print(get_data())
    return None

def main() -> None:
    test()
    return None

if __name__ == '__main__':
    main()

    


        
