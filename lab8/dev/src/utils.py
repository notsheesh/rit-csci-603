import tkinter as tk
import sys, os, math, re

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def is_square(n):
    return n > 0 and int(n**0.5)**2 == n

def is_valid_pixel(n):
    if n == -1:
        return True 
    else: 
        if (n >= 0 and n <= 255):
            return True
        else:
            return False

def is_integer(s):
    if s == "-1":
        return True
    else: 
        pattern = re.compile(r'^[0-9]+$')
        match = pattern.search(s)
        return bool(match)

def parse_args():
    num_args = len(sys.argv)
    args = sys.argv

    # uncompressed mode
    if num_args == 2:
        if args[1] != "-c":
            filename = args[1]
            mode = "uncompressed"
        else:
            error_state()

    # compressed mode
    elif num_args == 3:
        if args[1] == "-c":
            filename = args[2]
            mode = "compressed"
        else:
            error_state()
        
    else:
        error_state()
    
    filepath = os.path.join("../", "images", mode, filename)
    # size = int(filename.split('.')[0].split('x')[1])
    # title = filename.split(filename.split('.')[0].split('x')[1])[0]
    # height = math.log2(int(filename.split('.')[0].split('x')[1]))

    return {
        'mode': mode,
        'filename': filename,
        'filepath': filepath,
        # 'size': size,
        # 'height': height,
        'size': -1,
        'height': -1,
        'title': filename,
    }

def dump_data(arr, filename):
    filename = filename.split('.')[0] + '.txt'
    filepath = os.path.join('../', 'images', 'compressed', 'dump', filename)

    with open(filepath, 'w') as file:
        for i, element in enumerate(arr):
            file.write(str(element) + '\n')    

def error_state():
    msg = "Usage: python image_viewer.py [-c] <filename>\n"
    msg += "    "
    msg += "-c Reads in a compressed image file. If this option is not present,\n"
    msg += "        the file is considered to be uncompressed."
    print(msg)
    sys.exit(-1)    

