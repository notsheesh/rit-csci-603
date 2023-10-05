import turtle

ttl = turtle.Turtle()
screen = turtle.Screen()
screen.setup( width=1.0, height=1.0 ) 
screen.title("hello")
ttl.dot(100)

turtle.exitonclick()
input()
turtle.mainloop()