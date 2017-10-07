import random
import turtle
import math
jerry = turtle.Turtle()
print(jerry)
def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    #draws a circle so the user can see the origin
    jerry.circle(5)
    ns = 0
    ew = 0
    ns_direction = ''
    ew_direction = ''
    for block in range(n):
        direction = random.randrange(0,4)
        if direction == 0:
            ns += 1
            print('drunkard walks north')
            jerry.setheading(90)
        elif direction == 1:
            ew += 1
            print('drunkard walks east')
            jerry.setheading(0)
        elif direction == 2:
            ns -= 1
            print('drunkard walks south')
            jerry.setheading(270)
        else:
            ew -= 1
            print('drunkard walks west')
            jerry.setheading(180)
        jerry.fd(30)
       
    if ns >= 0:
        ns_direction = 'north'
    else:
        ns_direction = 'south'
    if ew >= 0:
        ew_direction = 'east'
    else:
        ew_direction = 'west'
    print('The drunkard has moved a total distance of %s block(s) to the %s and %s block(s) to the %s' %(abs(ns), ns_direction, abs(ew), ew_direction))

    while True:
        jerry.lt(2)

drunkard(70)
print("The drunkard started from (%d,%d)." % (x, y))
distance = drunkard_walk(x, y, n)
print(" After", n, "intersections, he's",
      distance, "blocks from where he started.")

turtle.mainloop()