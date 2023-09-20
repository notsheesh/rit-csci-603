"""
CSCI-603 Lab 3: Islands

A program that uses turtle graphics to draw fractal islands of two different 
types. The user can specify the number of sides, the length of the initial side,
and the number of recursion levels to generate complex island shapes.

author: Shreesh Tripathi, st4083
"""
import turtle
import math
import sys
import re

ttl = None  # turtle object
# Patterns for input validation
POS_INT = r'^[1-9]\d*$'
NEG_INT = r'^-\d+$'
ZERO_INT = r'^0$'

POS_FLOAT = r'^[1-9]\d*\.\d+$'
NEG_FLOAT = r'^-\d+\.\d+$'
ZERO_FLOAT = r'^0\.\d+$'

STR = r'^[a-zA-Z]+$'


def draw_fractal_curve_1 ( 
        length: float,
        level: int,
        perimeter: float = 0 ) -> float :
    """
    Draws a fractal curve of type 1 using recursive calls.

    :param length: Length of the initial side.
    :param level: Number of recursion levels.
    :param perimeter: Current perimeter value.

    :return: Total perimeter value.
    """

    if level == 1:
        ttl.forward ( length ) 
        perimeter += length
        return perimeter
    else:
        perimeter = draw_fractal_curve_1 ( length / 3, level - 1, perimeter ) 
        ttl.left ( 60 ) 
        perimeter = draw_fractal_curve_1 ( length / 3, level - 1, perimeter ) 
        ttl.right ( 120 ) 
        perimeter = draw_fractal_curve_1 ( length / 3, level - 1, perimeter ) 
        ttl.left ( 60 ) 
        perimeter = draw_fractal_curve_1 ( length / 3, level - 1, perimeter ) 

    return perimeter


def draw_fractal_curve_2 ( 
        length: float,
        level: int,
        perimeter: float = 0 ) -> float :
    """
    Draws a fractal curve of type 2 using recursive calls.

    :param length: Length of the initial curve segment.
    :param level: Number of recursion levels.
    :param perimeter: Current perimeter value.

    :return: Total perimeter value.
    """

    if level == 1:
        ttl.forward ( length ) 
        perimeter += length
        return perimeter
    else:
        ttl.left ( 45 ) 
        perimeter = draw_fractal_curve_2 ( 
            length / 2 / math.cos ( math.pi / 4 ) , level - 1, perimeter ) 
        ttl.right ( 90 ) 
        perimeter = draw_fractal_curve_2 ( 
            length / 2 / math.cos ( math.pi / 4 ) , level - 1, perimeter ) 
        ttl.left ( 45 ) 

    return perimeter


def draw_island_1 ( 
        num_sides: int,
        side_length: float,
        num_levels: int ) -> float :
    """
    Draws an island-like shape using the fractal curve 1.

    :param num_sides: Number of sides in the island.
    :param side_length: Length of the initial side.
    :param num_levels: umber of recursion levels.

    :return: The total perimeter of the island.
    """
    perimeter = 0
    for _ in range ( num_sides ) :
        perimeter += draw_fractal_curve_1 ( side_length, num_levels ) 
        ttl.left ( 360 / num_sides ) 
    return perimeter


def draw_island_2 ( 
        num_sides: int,
        side_length: float,
        num_levels: int ) -> float :
    """
    Draws an island-like shape using the fractal curve 2.

    :param num_sides: Number of sides in the island.
    :param side_length: Length of the initial side.
    :param num_levels: umber of recursion levels.

    :return: The total perimeter of the island.
    """
    perimeter = 0
    for _ in range ( num_sides ) :
        perimeter += draw_fractal_curve_2 ( side_length, num_levels ) 
        ttl.left ( 360 / num_sides ) 
    return perimeter


def which_type ( input_val: str ) -> str :
    """
    Determines the data type of an input value using regular expressions.

    :param input_val: The input value to be checked.

    :return: A string representing the data type of the input value.
    """
    if re.fullmatch ( POS_INT, input_val ) :
        return "positive integer-value"
    # Not required, only for completeness
    if re.fullmatch ( NEG_INT, input_val ) :
        return "negative integer-value"
    # Not required, only for completeness
    if re.fullmatch ( ZERO_INT, input_val ) :
        return "zero integer-value"
    if re.fullmatch ( POS_FLOAT, input_val ) :
        return "positive float-value"
    # Not required, only for completeness
    if re.fullmatch ( NEG_FLOAT, input_val ) :
        return "negative float-value"
    # Not required, only for completeness
    if re.fullmatch ( ZERO_FLOAT, input_val ) :
        return "zero float-value"
    if re.fullmatch ( STR, input_val ) :
        return "string-value"
    # Not required, only for completeness
    else:
        return "unknown value"


def is_pos_float ( input_val: str ) -> bool:
    """
    Checks if an input value is a positive float.

    :param input_val: The input value to be checked.

    :return: True if the input is a positive float, False otherwise.
    """
    if re.fullmatch ( POS_FLOAT, input_val ) :
        return True
    else:
        data_type = which_type ( input_val ) 
        print ( "Value must be a positive float."
                " You entered a '{}'".format ( data_type ) ) 
        return False


def is_pos_int ( input_val: str ) -> bool:
    """
    Checks if an input value is a positive integer.

    :param input_val: The input value to be checked.

    :return: True if the input is a positive integer, False otherwise.
    """
    if re.fullmatch ( POS_INT, input_val ) :
        return True
    else:
        data_type = which_type ( input_val ) 
        print ( "Value must be a positive integer."
                " You entered a '{}'".format ( data_type ) ) 
        return False


def take_user_input_num_sides() -> int:
    """
    Takes user input for the number of sides of the island.

    :return: User-provided number of sides as an integer.
    """
    if len ( sys.argv ) > 1:
        return int ( sys.argv[ 1 ] ) 

    while True:
        num_sides = input ( "Number of sides: " ) 
        if is_pos_int ( num_sides ) :
            return int ( num_sides ) 
        else:
            continue


def take_user_input_side_length() -> float :
    """
    Takes user input for the length of the initial side.

    :return: User-provided length as a float.
    """
    if len ( sys.argv ) > 1:
        return float ( sys.argv[ 2 ] ) 

    while True:
        side_length = input ( "Length of initial side: " ) 
        if is_pos_float ( side_length ) :
            return float ( side_length ) 
        else:
            continue


def take_user_input_num_levels() -> int:
    """
    Takes user input for the number of recursion levels.

    :return: User-provided number of levels as an integer.
    """
    if len ( sys.argv ) > 1:
        return int ( sys.argv[ 3 ] ) 

    while True:
        num_levels = input ( "Number of levels: " ) 
        if is_pos_int ( num_levels ) :
            return int ( num_levels ) 
        else:
            continue


def take_user_input() -> list:
    """
    Takes user input for the number of sides, side length, and recursion levels.
    """
    num_sides = take_user_input_num_sides() 
    side_length = take_user_input_side_length() 
    num_levels = take_user_input_num_levels() 
    return num_sides, side_length, num_levels


def main() :
    """
    Driver function for taking user input and drawing of fractal curve islands.
    """
    global ttl

    # Take user input
    num_sides, side_length, num_levels = take_user_input() 

    # Setup turtle screen
    ttl = turtle.Turtle() 
    ttl.speed ( 0 ) 
    turtle.Screen().setup( width=1.0, height=1.0 ) 

    # Draw island 1
    # turtle.tracer ( 0, 0 )
    island_1_perimeter = draw_island_1 ( num_sides, side_length, num_levels ) 
    # turtle.update() 
    print ( "Curve 1 - Island’s length is "
            "{} units.".format ( island_1_perimeter ) ) 

    # Wait for user input and reset
    input ( "Hit enter to continue..." ) 
    ttl.reset() 

    # Draw island 2
    # turtle.tracer ( 0, 0 )
    island_2_perimeter = draw_island_2 ( num_sides, side_length, num_levels ) 
    # turtle.update() 
    print ( "Curve 2 - Island’s length is "
            "{} units.".format ( island_2_perimeter ) ) 

    # End
    print ( "Bye!" ) 

    # Hit enter to close turtle screen
    input() 
    turtle.bye() 


if __name__ == '__main__':
    main() 
