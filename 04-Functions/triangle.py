import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(3)

def draw_triangle(a):
    for _ in range(3):
        pen.forward(a)
        pen.left(120)

draw_triangle(150)

# Finish
window.mainloop()