import turtle
import math

ttl = turtle.Turtle()
turtle.Screen().setup(width=1.0, height=1.0)

length = 300
breadth = 10
small_sq_side1 = length/4
small_sq_side2 = length/8
tilted_sq_side = ((small_sq_side2 /  2) / math.cos(math.pi/4)) * 2
offset = 180 # where to go before starting figure 1

ttl.speed(0)

def drawRectangle(length, breadth):
    ttl.pendown()
    for i in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(breadth)
        ttl.left(90)

def drawSquareBorder(length, breadth):
    ttl.pendown()
    for i in range(4):
        drawRectangle(length, breadth)
        ttl.penup()
        ttl.forward(length)
        ttl.left(90)
        ttl.pendown()

def drawTriangle(base, side, theta):
    ttl.pendown()
    ttl.forward(base)
    ttl.left(90)
    ttl.left(theta)
    ttl.forward(side)
    ttl.left(2*(90-theta))
    ttl.forward(side)
    ttl.left(90)
    ttl.left(theta)

# main code starts here 

# pre condition for figure 1
ttl.penup()
ttl.right(90)
ttl.forward(length/2)
ttl.right(90)
ttl.forward(length+offset)
ttl.right(180)

# draw square border
drawSquareBorder(length, breadth)

# precondition for inner square
ttl.penup()
ttl.forward(length/2)
ttl.left(90)
ttl.forward(length/2)
ttl.left(90)
ttl.forward(small_sq_side1/2)
ttl.left(90)
ttl.forward(small_sq_side1/2)
ttl.left(90)

# start drawing inner square
ttl.fillcolor("#FF1493")
ttl.begin_fill()
drawRectangle(small_sq_side1, small_sq_side1)
ttl.end_fill()

# pre condition for windmill
ttl.penup()
ttl.forward(small_sq_side1/2)
ttl.left(90)
ttl.forward(small_sq_side1/2)
ttl.right(90)

# start drawing windmill 
triangle_base = small_sq_side1
triangle_side = (small_sq_side1 / 2) * (2 ** 0.5)
triangle_theta = abs(
    math.degrees(
        math.atan(
                (small_sq_side1/2)
                / (small_sq_side1/2)
        )
    )
)

ttl.fillcolor("#9F2B68")
ttl.begin_fill()

for _ in range(4):
    drawTriangle(triangle_base, triangle_side, triangle_theta)
    ttl.left(90)

ttl.end_fill()

# go back to pre condition figure 1 
ttl.penup()
ttl.right(90)
ttl.forward(length/2)
ttl.right(90)
ttl.forward(length/2)
ttl.right(180)

# pre condition for figure 2
offset = 30
ttl.penup()
ttl.forward(length)
ttl.forward(offset)

# draw border for figure 2
drawSquareBorder(length, breadth)

# precondition for inner square 2 
ttl.penup()
ttl.forward(length/2)
ttl.left(90)
ttl.forward(length/2)
ttl.left(90)
ttl.forward(small_sq_side2/2)
ttl.left(90)
ttl.forward(small_sq_side2/2)
ttl.left(90)

# pre condition for tilted square
ttl.penup()
ttl.right(45)
ttl.forward(tilted_sq_side/2)
ttl.left(90)

# draw tilted square
ttl.fillcolor("#00ffef")
ttl.begin_fill()
drawRectangle(tilted_sq_side, tilted_sq_side)
ttl.end_fill()

# post condition for tilted square
ttl.left(90)
ttl.forward(tilted_sq_side/2)
ttl.right(45+90)

# draw inner square
ttl.fillcolor("#00008b")
ttl.begin_fill()
drawRectangle(small_sq_side2, small_sq_side2)
ttl.end_fill()

# hourglass
hour_glass_base = tilted_sq_side * ( 2 ** 0.5 ) / 2
def drawHourGlass(hour_glass_base, tilted_sq_side):
    ttl.pendown()
    ttl.right(45)
    ttl.forward(tilted_sq_side)
    ttl.left(45+90)
    ttl.forward(hour_glass_base)
    ttl.left(45+90)
    ttl.forward(tilted_sq_side)
    ttl.right(90+45)
    ttl.forward(hour_glass_base)
    ttl.right(90)

ttl.fillcolor("#800020")
for _ in range(4):
    ttl.begin_fill()
    drawHourGlass(hour_glass_base, tilted_sq_side)
    ttl.end_fill()
    ttl.penup()
    ttl.forward(small_sq_side2)
    ttl.left(90)

# post condition for figure 2
ttl.forward(small_sq_side2/2)
ttl.left(90)
ttl.forward(small_sq_side2/2)
ttl.left(180)
ttl.forward(length/2)
ttl.right(90)
ttl.forward(length/2)
ttl.left(180)

# pre condition for third figure
offset = 30
ttl.penup()
ttl.forward(length)
ttl.forward(offset)

drawSquareBorder(length, breadth)


# Close the turtle graphics window when clicked
turtle.exitonclick()
