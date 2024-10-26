import turtle
from draw_figures import side_length

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def draw_triangle():
    for _ in range(3):
        pen.forward(side_length)
        pen.right(120)

draw_triangle(side_length)

# Finish
window.mainloop()