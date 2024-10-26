import turtle
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

def draw_rectangle(a,b):
    for _ in range (2):
        pen.forward(a)
        pen.left(90)
        pen.forward(b)
        pen.left(90)
draw_rectangle(200,75)

window.mainloop()