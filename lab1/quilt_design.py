"""
file: quilt.py
description: csci 603 cps, lab 1
language: python3
author: shreesh tripathi, st4083@rit.edu
"""
import turtle
import math

# Screen configuration
turtle.Screen().setup(width=1.0, height=1.0)

# Turtle speed
ttl = turtle.Turtle()
ttl.speed(0)

# Global constants
RIGHT_ANGLE_DEG = 90  # Right angle in degrees

# Border constants
BORDER_LENGTH = 300
BORDER_MARGIN = 10
FIGURE_GAP = 30  # Gap between two figures

# Figure 1 constants
FIG1_SQ_SIDE = BORDER_LENGTH / 4  # Square length
WINDMILL_BASE = FIG1_SQ_SIDE  # Triangle base
WINDMILL_SIDE = FIG1_SQ_SIDE / math.sqrt(2)  # Triangle adjacent side
WINDMILL_THETA = RIGHT_ANGLE_DEG / 2  # Triangle angle

# Figure 2 constants
FIG2_SQ_A_SIDE = BORDER_LENGTH / 8  # Square length
FIG2_SQ_B_SIDE = FIG2_SQ_A_SIDE * math.sqrt(2)  # Tilted square length
HOUR_GLASS_BASE = FIG2_SQ_B_SIDE / math.sqrt(2)  # Hour glass base

# Figure 3 constants
PETAL_LENGTH = BORDER_LENGTH / 4  # Petal length
PETAL_BREADTH = 5  # Petal breadth

FIGURE_OFFSET = 180  # Offset for figure 1 precondition

""" General Helper Functions """


def draw_rectangle(length, breadth):
    """
    Draw a rectangle for the given length and breadth

    Pre Condition: Bottom left corner of square
    Post Condition: Bottom left corner of square

    :param length: what is the length of the rectangle
    :param breadth: what is the breadth of the rectangle
    :return: None
    """
    ttl.pendown()
    for i in range(2):
        ttl.forward(length)
        ttl.left(RIGHT_ANGLE_DEG)
        ttl.forward(breadth)
        ttl.left(RIGHT_ANGLE_DEG)


def draw_sq_border(length, margin):
    """
    Draw a double lined square border with the given length and margin

    Pre Condition: Bottom left corner of square
    Post Condition: Bottom left corner of square

    :param length: what is the length of the outter square
    :param margin: what is the margin of the inner square
    :return: None
    """
    ttl.pendown()
    for i in range(4):
        draw_rectangle(length, margin)
        ttl.penup()
        ttl.forward(length)
        ttl.left(RIGHT_ANGLE_DEG)
        ttl.pendown()


def go_to_sq_center(square_side):
    """
    Go to the square center from the bottom left corner of the square

    Pre Condition: Bottom left corner of square
    Post Condition: Center of square

    :param square_side: what is the length of the square 
    :return: None
    """
    ttl.penup()
    ttl.forward(square_side / 2)
    ttl.left(RIGHT_ANGLE_DEG)
    ttl.forward(square_side / 2)
    ttl.right(RIGHT_ANGLE_DEG)


def go_back_to_sq_corner(square_side):
    """
    Go to the square bottom corner from the center of the square

    Pre Condition: Center of square
    Post Condition: Bottom left corner of square

    :param square_side: what is the length of the square 
    :return: None
    """
    ttl.penup()
    ttl.right(RIGHT_ANGLE_DEG)
    ttl.forward(square_side / 2)
    ttl.right(RIGHT_ANGLE_DEG)
    ttl.forward(square_side / 2)
    ttl.right(180)


""" Figure 1 Helper Functions """


def set_figure1_precondition():
    """
    Set the turtle state and precondition for turtle 1

    Pre Condition: Center of canvas
    Post Condition: 
        X coordinate: - (BORDER_LENGTH + FIGURE_OFFSET)
        Y coordinate: BORDER_LENGTH / 2

    :param: None 
    :return: None
    """
    ttl.penup()
    ttl.right(RIGHT_ANGLE_DEG)
    ttl.forward(BORDER_LENGTH / 2)
    ttl.right(RIGHT_ANGLE_DEG)
    ttl.forward(BORDER_LENGTH + FIGURE_OFFSET)
    ttl.right(180)


def draw_figure1_square():
    """
    Draw the figure 1 inner square
    Color: #FF1493
    Side: FIG1_SQ_SIDE

    Pre Condition: Bottom left corner of square
    Post Condition: Bottom left corner of square

    :param: None 
    :return: None
    """
    ttl.fillcolor("#FF1493")
    ttl.begin_fill()
    draw_rectangle(FIG1_SQ_SIDE, FIG1_SQ_SIDE)
    ttl.end_fill()


def draw_triangle(base, side, theta):
    """
    Draw a triangle component

    Pre Condition = Post Condition = bottom left vertice of triangle

    :param base: what is the base of the triangle
    :param side: what is the adjacent side of the triangle
    :param theta: what is the angle of the triangle
    :return: None
    """
    ttl.pendown()
    ttl.forward(base)
    ttl.left(RIGHT_ANGLE_DEG + theta)
    ttl.forward(side)
    ttl.left(2*(RIGHT_ANGLE_DEG-theta))
    ttl.forward(side)
    ttl.left(RIGHT_ANGLE_DEG + theta)


def draw_windmill():
    """
    Draw a windmill pattern by using four iterations of triangle components and
    90 degree turns

    Color: #9F2B68
    Base: WINDMILL_BASE

    Pre Condition = Post Condition = center of figure 1

    :param: None 
    :return: None
    """
    ttl.fillcolor("#9F2B68")
    ttl.begin_fill()
    for _ in range(4):
        draw_triangle(WINDMILL_BASE, WINDMILL_SIDE, WINDMILL_THETA)
        ttl.left(RIGHT_ANGLE_DEG)
    ttl.end_fill()


""" Figure 2 Helper Functions """


def draw_figure2_a_square():
    """
    Draw the figure 2 square using draw_rectangle() method
    Color: #00008b
    Side: FIG1_SQ_SIDE

    Pre Condition: Bottom left corner of square
    Post Condition: Bottom left corner of square

    :param: None 
    :return: None
    """
    ttl.fillcolor("#00008b")
    ttl.begin_fill()
    draw_rectangle(FIG2_SQ_A_SIDE, FIG2_SQ_A_SIDE)
    ttl.end_fill()


def draw_figure2_b_tilted_sq():
    """
    Draw the figure 2 tilted square after tilting by 'Tilt' angle using the 
    draw_rectangle() function 
    Color: #FF1493
    Side: FIG1_SQ_SIDE
    Tilt: RIGHT_ANGLE_DEG / 2

    Pre Condition: Bottom left corner of square
    Post Condition: Bottom left corner of square

    :param: None 
    :return: None
    """
    # Pre Condition
    ttl.penup()
    ttl.right(RIGHT_ANGLE_DEG / 2)
    ttl.forward(FIG2_SQ_B_SIDE / 2)
    ttl.left(RIGHT_ANGLE_DEG)

    ttl.fillcolor("#00ffef")
    ttl.begin_fill()
    draw_rectangle(FIG2_SQ_B_SIDE, FIG2_SQ_B_SIDE)
    ttl.end_fill()

    # Post Condition
    ttl.left(RIGHT_ANGLE_DEG)
    ttl.forward(FIG2_SQ_B_SIDE / 2)
    ttl.right(RIGHT_ANGLE_DEG / 2 + RIGHT_ANGLE_DEG)


def draw_hour_glass(base, slope_length):
    """
    Draw an hour glass component 

    Pre Condition = Post Condition = bottom left vertice of hour glass

    :param base: what is the base of hour glass component
    :param slope_length: what is the slope of the hour glass component
    :return: None
    """
    ttl.pendown()
    ttl.right(RIGHT_ANGLE_DEG / 2)
    ttl.forward(slope_length)
    ttl.left(RIGHT_ANGLE_DEG / 2 + RIGHT_ANGLE_DEG)
    ttl.forward(base)
    ttl.left(RIGHT_ANGLE_DEG / 2 + RIGHT_ANGLE_DEG)
    ttl.forward(slope_length)
    ttl.right(RIGHT_ANGLE_DEG + RIGHT_ANGLE_DEG / 2)
    ttl.forward(base)
    ttl.right(RIGHT_ANGLE_DEG)


def draw_hour_glass_pattern():
    """
    Draw the hour glass pattern using 4 iterations over the hour glass component

    Pre Condition = Post Condition = bottom left vertice of hour glass

    Color: #800020
    Base: HOUR_GLASS_BASE
    Slope Length: FIG2_SQ_B_SIDE
    :param: None 
    :return: None
    """
    ttl.fillcolor("#800020")
    for _ in range(4):
        ttl.begin_fill()
        draw_hour_glass(HOUR_GLASS_BASE, FIG2_SQ_B_SIDE)
        ttl.end_fill()
        ttl.penup()
        ttl.forward(FIG2_SQ_A_SIDE)
        ttl.left(RIGHT_ANGLE_DEG)


""" Figure 2 Helper Functions """


def draw_figure3_pattern():
    """
    Draw figure 3 pattern by iterating over tilted rectangles 36 times while 
    changing the angle by 10 degrees after every iteration. This will be 
    followed by drawing an overlapping black circle to enforce symmetry

    Pre Condition = Center of border 3 
    Post Condition = Bottom left corner of figure 3 

    Colors: Black, White 
    :param: None 
    :return: None
    """
    ttl.pendown()
    colors = ["black", "white"]
    for i in range(2):
        for j in range(36):
            ttl.fillcolor(colors[i])
            ttl.begin_fill()
            draw_rectangle(PETAL_LENGTH / (i + 1), PETAL_BREADTH)
            ttl.end_fill()
            ttl.left(10)

    radius = 15
    ttl.fillcolor("black")

    # Pre Condition for circle
    ttl.forward(radius)
    ttl.left(RIGHT_ANGLE_DEG)

    # Draw circle
    ttl.begin_fill()
    ttl.circle(radius)
    ttl.end_fill()
    ttl.right(RIGHT_ANGLE_DEG)
    ttl.backward(radius)


#################### Main code starts here ###################
if __name__ == '__main__':
    #################### Figure 1 starts here ####################
    # Figure 1 border
    set_figure1_precondition()  # Pre Condition figure 1
    draw_sq_border(BORDER_LENGTH, BORDER_MARGIN)  # Draw figure 1 border
    go_to_sq_center(BORDER_LENGTH)  # Precondition for figure 1 square
    go_back_to_sq_corner(FIG1_SQ_SIDE)

    # Figure 1 square
    draw_figure1_square()  # Draw figure 1 square

    # Figure 1 windmill
    go_to_sq_center(FIG1_SQ_SIDE)  # Pre Condition for windmill
    draw_windmill()  # Draw windmill over square
    go_back_to_sq_corner(BORDER_LENGTH)  # Post Condition for figure 1
    #################### Figure 1 ends here ####################

    #################### Figure 2 starts here ##################
    # Figure 2 border
    ttl.penup()
    # Pre Condition for figure 2 border
    ttl.forward(BORDER_LENGTH + FIGURE_GAP)
    draw_sq_border(BORDER_LENGTH, BORDER_MARGIN)  # Draw figure 2 border

    # Figure 2 tilted square
    # Pre Condition for tilted square
    go_to_sq_center(BORDER_LENGTH)
    go_back_to_sq_corner(FIG2_SQ_A_SIDE)

    # Draw tilted square
    draw_figure2_b_tilted_sq()

    # draw inner square
    draw_figure2_a_square()

    # Draw hour glass pattern
    draw_hour_glass_pattern()

    # Post Condition for Figure 2
    go_to_sq_center(FIG2_SQ_A_SIDE)
    go_back_to_sq_corner(BORDER_LENGTH)
    #################### Figure 2 ends here ####################

    #################### Figure 3 starts here ##################
    # Figure 3 border
    ttl.penup()
    # Pre Condition for figure 3 border
    ttl.forward(BORDER_LENGTH + FIGURE_GAP)
    draw_sq_border(BORDER_LENGTH, BORDER_MARGIN)  # Draw figure 3 border

    # Pre Condition for figure 3 pattern
    go_to_sq_center(BORDER_LENGTH)

    # Draw figure 3 pattern
    draw_figure3_pattern()

    # Post Condition of figure 3
    go_back_to_sq_corner(BORDER_LENGTH)
    #################### Figure 3 ends here ####################

    #################### Figure 4 starts here ##################

    # Uncomment for figure 4
    # # Figure 4 border
    # ttl.penup()
    # ttl.forward(BORDER_LENGTH + FIGURE_GAP) # Pre Condition for figure 4 border
    # draw_sq_border(BORDER_LENGTH, BORDER_MARGIN) # Draw figure 4 border

    #################### Figure 4 ends here ####################

turtle.exitonclick()  # Close the turtle when clicked
