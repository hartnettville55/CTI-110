# Travis Hartnett
# 18 October 2026
# P4LAB1
# Draw a square and a triangle to create a house using turtle and loops

import turtle

# Create window and drawing object
win = turtle.Screen ()
pen = turtle.Turtle ()
win.bgcolor("teal")

# Setting turtle options
pen.pensize (5)
pen.pencolor ("blue")
pen.shape ("arrow")

#Code to draw triangle and square
pen.fillcolor("white")
pen.begin_fill ()
for side in range (4) :
    pen.forward (200)
    pen.right (90)
pen.end_fill ()

#while loop for the triangle

sides = 3
pen.fillcolor("orange")
pen.begin_fill()


while sides > 0:
    pen.forward (200)
    pen.left (120)
    sides = sides - 1
pen.end_fill()

#user closes window
win.mainloop ()