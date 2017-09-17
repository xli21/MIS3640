import turtle

Xiang = turtle.Turtle()
print(Xiang) 

#for i in range(4):
    #Xiang.fd(100)
    #Xiang.lt(90)


#turtle.mainloop()


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(Xiang, 50, 20)

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


arc(Xiang, 100, 180)

turtle.mainloop()
