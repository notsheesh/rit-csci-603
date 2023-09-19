import turtle
import math
ttl = turtle.Turtle()
turtle.Screen().setup(width=1.0, height=1.0)
ttl.speed(0)

COS_45 = math.cos(math.pi/4)
def one_side(n):
    ttl.forward(n)

def two_side(n): # lfrfl 
    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.left(45)

def three_levels(n):
    ttl.left(45)
    two_side(n)
    ttl.right(90)
    two_side(n)
    ttl.left(45)

def four_levels(n):
    ttl.left(45)
    three_levels(n)
    ttl.right(90)
    three_levels(n)
    ttl.left(45)

def five_levels(n):
    ttl.left(45)
    four_levels(n)
    ttl.right(90)
    four_levels(n)
    ttl.left(45)

def n_levels(n, level):
    if level == 1:
        ttl.forward(n)
        return
    else:
        ttl.left(45)
        n_levels(n/COS_45, level - 1)
        ttl.right(90)
        n_levels(n/COS_45, level - 1)
        ttl.left(45)

ttl.penup()
ttl.backward(300)
# ttl.right(90)
# ttl.forward(200)
# ttl.left(90)
ttl.pendown()

n = 2
level = 8
# two_side(n)
# three_levels(n)
# four_levels(n)
# five_levels(n)
n_levels(n, level)

turtle.done()
    

    