import turtle 
ttl = turtle.Turtle()

turtle.Screen().setup(width=1.0, height=1.0)
ttl.speed(0)

def draw_side1(n: float) -> None:
    ttl.forward(n)

def draw_side2(n: float) -> None:
    ttl.forward(n/4)
    ttl.left(45)
    draw_side1(n*(2**0.5)/4)
    ttl.right(90)
    draw_side1(n*(2**0.5)/4)
    ttl.left(45)
    ttl.forward(n/4)

def draw_side(n: float, level: int) -> None:
    if level == 1:
        ttl.forward(n)
        return
    else: 
        ttl.forward(n/4)
        ttl.left(45)
        draw_side(n * (2**0.5)/4, level-1)
        ttl.right(90)
        draw_side(n * (2**0.5)/4, level-1)
        ttl.left(45)
        ttl.forward(n/4)

# pre condition
ttl.penup()
ttl.backward(400)
ttl.pendown()

# main
n = 500
level = 7
draw_side(n, level)
draw_side2(n)

turtle.done()