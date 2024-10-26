import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def draw_square(length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
# Draw a square
draw_square(100)

pen.penup()
pen.goto(-100, 100)
pen.down()

def draw_square(length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
# Draw a square
draw_square(100)

pen.penup()
pen.goto(200, -200)
pen.down()

def draw_rectangle(a,b):
    for _ in range (2):
        pen.forward(a)
        pen.left(90)
        pen.forward(b)
        pen.left(90)
draw_rectangle(150,75)

pen.penup()
pen.goto(200, 100)
pen.down()

def draw_rectangle(a,b):
    for _ in range (2):
        pen.forward(a)
        pen.left(90)
        pen.forward(b)
        pen.left(90)
draw_rectangle(-150,75)

pen.penup()
pen.goto(-200, -150)
pen.down()

def draw_triangle(a):
    for _ in range(3):
        pen.forward(a)
        pen.left(120)
draw_triangle(150)

pen.penup()
pen.goto(-300, 150)
pen.down()

def draw_triangle(a):
    for _ in range(3):
        pen.forward(a)
        pen.left(120)
draw_triangle(150)

# Finish
window.mainloop()