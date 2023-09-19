import turtle
import math
ttl = turtle.Turtle()
turtle.Screen().setup(width=1.0, height=1.0)
# ttl.speed(0)

# fc 1
# level 1
def draw_side1_fc1(n):
    ttl.forward(n)

# level 2
def draw_side2_fc1(n):
    ttl.forward(n/3)
    ttl.left(60)
    ttl.forward(n/3)
    ttl.right(120)
    ttl.forward(n/3)
    ttl.left(60)
    ttl.forward(n/3)

# level 3
def draw_side3_fc1(n):
    draw_side2_fc1(n/3)
    ttl.left(60)
    draw_side2_fc1(n/3)
    ttl.right(120)
    draw_side2_fc1(n/3)
    ttl.left(60)
    draw_side2_fc1(n/3)

# level 4
def draw_side4_fc1(n):
    draw_side3_fc1(n/3)
    ttl.left(60)
    draw_side3_fc1(n/3)
    ttl.right(120)
    draw_side3_fc1(n/3)
    ttl.left(60)
    draw_side3_fc1(n/3)

# level n
def draw_side_fc1(level, n):
    if level == 1:
        ttl.forward(n)
        return
    else:
        draw_side_fc1(level-1, n/3)
        ttl.left(60)
        draw_side_fc1(level-1, n/3)
        ttl.right(120)
        draw_side_fc1(level-1, n/3)
        ttl.left(60)
        draw_side_fc1(level-1, n/3)

# pre condition
def pre_condition(n):
    ttl.penup()
    ttl.backward(n/2)
    ttl.right(90)
    ttl.forward(100)
    ttl.left(90)
    ttl.pendown()


# n = 1000
# level = 5
# pre_condition(n)
# fc 1
# draw_side1_fc1(n)
# draw_side2_fc1(n)
# draw_side3_fc1(n)
# draw_side4_fc1(n)
# draw_side_fc1(level, n)


turtle.done()
    

    