import turtle
import math
ttl = turtle.Turtle()
turtle.Screen().setup(width=1.0, height=1.0)
# ttl.speed(0)

COS_45 = math.cos(math.pi/4)
def one_side(n):
    ttl.forward(n)

def two_side(n):
    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.left(45)

def three_sides(n):
    ttl.left(45)

    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)

    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.left(45)
    ttl.left(45)

def four_sides(n):
    ttl.left(45)
    ttl.left(45)
    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.left(45)
    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.left(45)
    ttl.left(45)
    ttl.left(45)

def five_sides(n):
    ttl.left(45)
    ttl.left(45)
    ttl.left(45)
    ttl.left(45)
    ttl.forward(n/COS_45)
    ttl.right(90)
    ttl.forward(n/COS_45)
    ttl.forward(n/COS_45)
    ttl.right(90)

ttl.penup()
ttl.backward(300)
ttl.right(90)
ttl.forward(200)
ttl.left(90)
ttl.pendown()

n = 100
# two_side(n)
# three_sides(n)
four_sides(n)

turtle.done()
    

    