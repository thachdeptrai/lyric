import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(5)
t.color("red")
t.hideturtle()

def heart_curve(t):
    x = 16* math.sin(t)**3
    y = 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x ,y

for scale in range(1, 11):
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in range(361):
        angle = math.radians(i)
        x, y = heart_curve(angle)
        t.goto(x*scale, y*scale)
turtle.done()


