import turtle
from draw_figures import side_length

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def draw_square():
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)
# Draw a square
draw_square(side_length)

# Finish
window.mainloop()