import turtle as t
import random

def screenLeftClick(x,y):
    tSize = random.randrange(2,10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r, g, b))
    tAngle = random.randrange(0, 360)

    t.penup()
    t.goto(x,y)
    t.left(tAngle)
    t.stamp()

pSize = 10
r, g, b, = 0.0, 0.0, 0.0

t.shape('turtle')
t.pensize(pSize)

t.onscreenclick(screenLeftClick, 1)

t.done()