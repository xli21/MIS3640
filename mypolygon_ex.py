import turtle

Xiang = turtle.Turtle()
print(Xiang) 

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

import math

def polyline( t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_leangth = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_leangth, step_angle)

def move(t, x, y):
    t.pu()
    t.setpos(x, y)
    t.pd()

circle (Xiang, 100)
move (Xiang, 0, 100)
Xiang.setheading(0)
arc(Xiang, 50, 180)

move (Xiang, 0, 100)
Xiang.setheading(180)
arc(Xiang, 50, 180)

move(Xiang, 0, 50 + 100 / 6)
circle(Xiang, 100 / 6)

move(Xiang, 0, 150 + 100 / 6)
circle(Xiang, 100 / 6)

turtle.mainloop()