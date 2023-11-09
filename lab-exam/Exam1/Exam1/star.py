'''
Author: Shreesh Tripathi, st4083
'''

import turtle 
import math
import re

# Housekeeping 
ttl = turtle.Turtle()
# ttl.speed(0)
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

def draw_square1(length):
    for _ in range(4):
        ttl.forward(length)
        ttl.left(90)

def draw_triangle1(length):
    for _ in range(3):
        ttl.forward(length)
        ttl.right(120)

def draw_square2(length):
    draw_square1(length)
    alpha = math.sqrt(2*(length/2)**2)
    theta = 45
    ttl.forward(length/2)
    ttl.left(theta)
    draw_square1(alpha)
    ttl.right(theta)
    ttl.backward(length/2)

def draw_star1(length):
    draw_square1(length)
    theta = 60
    beta = length / math.sqrt(3)
    offset = length/2 - beta/2
    for _ in range(4):
        ttl.forward(offset)
        draw_triangle1(beta)
        ttl.forward(length - offset)
        ttl.left(90)

def draw_nested_star(depth, length):
    if depth == 0:
        return
    else: 
        draw_star1(length)
        ttl.forward(length/2)
        ttl.left(45)
        length = math.sqrt(2*(length/2)**2)
        return draw_nested_star(depth-1, length)


def get_length_from_user():
    while True: 
        length = input("Please enter length: ")
        if re.fullmatch(r'^[1-9][0-9]*$', length):
            return int(length)
        else: 
            print("Enter valid positive integer")
        

def get_depth_from_user():
    while True: 
        depth = input("Please enter depth: ")
        if re.fullmatch(r'^[0-9][0-9]*$', depth):
            if int(depth) >= 0 and int(depth) <= 9:
                return int(depth)
            else: 
                print("Enter a value between 0 and 9 (included)")
        else: 
            print("Enter a valid integer")

def main():
    ######## Start of Solution ########
    length = 150
    depth = 6

    # Part 2 
    # draw_square1(length)
    # draw_triangle1(length)

    # Part 3 
    # draw_square2(length)

    # Part 4
    # draw_star1(length)

    # Part 5 
    length = get_length_from_user()
    depth = get_depth_from_user()
    draw_nested_star(depth, length)

    turtle.exitonclick()
    ######## End of Solution ########

if __name__ == '__main__':
    main()