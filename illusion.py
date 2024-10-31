from turtle import *
import colorsys

# Set up the drawing environment
bgcolor("white")  # Set background color
speed(0)  # Fastest drawing speed
hue = 0  # Starting hue for color transition

# Function to draw a star
def draw_star(size):
    for _ in range(5):  # A star has 5 points
        forward(size)
        right(144)  # Angle to create the star shape

# Draw swirling stars
for i in range(72):  # Number of stars
    color(colorsys.hsv_to_rgb(hue, 1, 1))  # Set color using HSV
    hue += 0.01  # Increment hue for color change
    
    penup()
    goto(0, 0)  # Move to center without drawing
    pendown()
    
    draw_star(100)  # Draw a star of size 100
    right(10)  # Rotate slightly for swirling effect
    forward(10)  # Move forward slightly to create distance between stars

# Close the window on click
exitonclick()  # This allows closing the window by clicking on it

done()  # Complete the drawing
