import turtle as t
t.screensize(10,10, bg="yellow")
t.setup(width=1500, height=700)

t.pensize(3)
t.shape('turtle')

t.penup()
t.goto(-200, -50)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(40, steps=3)
t.end_fill()

t.penup()
t.goto(-100, -50)
t.pendown()
t.begin_fill()
t.color("blue")
t.circle(40, steps=4)
t.end_fill()

t.penup()
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color("purple")
t.circle(100)
t.end_fill()

t.color("green")
t.penup()
t.goto(-100,50)
t.pendown()
t.write("도형 색칠하기", font=("Times",18,"bold"))


t.done()