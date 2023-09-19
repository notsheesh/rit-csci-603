import turtle
import math
ttl = turtle.Turtle()
turtle.Screen().setup(width=1.0, height=1.0)
ttl.speed(0)

COS_45 = math.cos(math.pi/4)
def draw_fractal_curve_2(length, level, perimeter=0):
    if level == 1:
        ttl.forward(length)
        perimeter += length
        return perimeter
    else:
        ttl.left(45)
        perimeter = draw_fractal_curve_2(length/COS_45, level - 1, perimeter)
        ttl.right(90)
        perimeter = draw_fractal_curve_2(length/COS_45, level - 1, perimeter)
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

def draw_island_1():
    perimeter = 0
    for _ in range(num_sides):
        perimeter += draw_fractal_curve_1(length, level)
        ttl.left(360/num_sides)
    print("Perimeter: " + str(perimeter))

def draw_island_2():
    perimeter = 0
    for _ in range(num_sides):
        perimeter += draw_fractal_curve_2(length, level)
        ttl.left(360/num_sides)
    print("Perimeter: " + str(perimeter))

turtle.tracer(0,0)
draw_island_1()
draw_island_2()
turtle.update()

turtle.done()