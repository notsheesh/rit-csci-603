import turtle
import math
import sys 

def draw_fractal_curve_2(length, level, perimeter=0):
    if level == 1:
        ttl.forward(length)
        perimeter += length
        return perimeter
    else:
        ttl.left(45)
        perimeter = draw_fractal_curve_2(
            length/2/math.cos(math.pi/4), level - 1, perimeter)
        ttl.right(90)
        perimeter = draw_fractal_curve_2(
            length/2/math.cos(math.pi/4), level - 1, perimeter)
        ttl.left(45)
    return perimeter

def draw_fractal_curve_1(length, level, perimeter=0):
    if level == 1:
        ttl.forward(length)
        perimeter += length
        return perimeter
    else:
        perimeter = draw_fractal_curve_1(length / 3, level - 1, perimeter)
        ttl.left(60)
        perimeter = draw_fractal_curve_1(length / 3, level - 1, perimeter)
        ttl.right(120)
        perimeter = draw_fractal_curve_1(length / 3, level - 1, perimeter)
        ttl.left(60)
        perimeter = draw_fractal_curve_1(length / 3, level - 1, perimeter)
    return perimeter

# pre condition
def pre_condition1(length):
    ttl.penup()
    ttl.backward(length/2)
    ttl.right(90)
    ttl.forward(100)
    ttl.left(90)
    ttl.pendown()

def pre_condition2():
    ttl.penup()
    ttl.backward(300)
    # ttl.right(90)
    # ttl.forward(200)
    # ttl.left(90)
    ttl.pendown()

length = 100
level = 6
num_sides = 8

def draw_island_1(num_sides, side_length, num_levels):
    perimeter = 0
    for _ in range(num_sides):
        perimeter += draw_fractal_curve_1(side_length, num_levels)
        ttl.left(360/num_sides)
    return perimeter

def draw_island_2(num_sides, side_length, num_levels):
    perimeter = 0
    for _ in range(num_sides):
        perimeter += draw_fractal_curve_2(side_length, num_levels)
        ttl.left(360/num_sides)
    return perimeter

def take_user_input_num_sides():
    # number of sides
    if len(sys.argv) > 1:
        return int(sys.argv[1])

    while True:
        try:
            num_sides = int(input("Number of sides: "))
        except ValueError:
            print("Invalid input. Enter a positive integer")
        else:
            if num_sides > 0:
                return num_sides
            else:
                print("Invalid input. Enter a positive integer")

def take_user_input_side_length():
    # side of length
    if len(sys.argv) > 1:
        return float(sys.argv[2])

    while True:
        try:
            side_length = float(input("Length of initial side: "))
        except ValueError:
            print("Invalid input. Enter a positive integer")
        else:
            if side_length > 0:
                return side_length
            else:
                print("Invalid input. Enter a positive integer")

def take_user_input_num_levels():
    # side of length
    if len(sys.argv) > 1:
        return int(sys.argv[3])

    while True:
        try:
            num_levels = int(input("Number of levels: "))
        except ValueError:
            print("Invalid input. Enter a positive integer")
        else:
            if num_levels > 0:
                return num_levels
            else:
                print("Invalid input. Enter a positive integer")

def main():

    num_sides = take_user_input_num_sides()
    side_length = take_user_input_side_length()
    num_levels = take_user_input_num_levels()


    # Setup turtle screen
    ttl = turtle.Turtle()
    ttl.speed(0)
    turtle.Screen().setup(width=1.0, height=1.0)
    turtle.tracer(0,0)
    # Draw island 1
    island_1_perimeter = draw_island_1(num_sides, side_length, num_levels)
    turtle.update()
    print("Curve 1 - Island’s length is {} units.".format(island_1_perimeter))

    # Wait for user input and reset
    input("Hit enter to continue...")
    ttl.reset()
    turtle.tracer(0,0)
    # Draw island 2
    island_2_perimeter = draw_island_2(num_sides, side_length, num_levels)
    print("Curve 2 - Island’s length is {} units.".format(island_2_perimeter))
    turtle.update()
    # End
    print("Bye!")
    turtle.exitonclick()
    
if __name__ == '__main__':
    main()