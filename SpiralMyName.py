# SpiralMyName.py
# Billy Ridgeway
# Prints a colorful spiral of the user's name.

import turtle               # Import turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the pen's speed to fast.
turtle.bgcolor("black")     # Sets the background color to black.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green"]

# Ask the user's name using turtle's text input pop-up window.
your_name = turtle.textinput("Enter your name", "What is your name?")

# Creates a for loop to draw a spiral of the user's name on the screen, written 100 times.
for x in range (100):               # Sets the value of x to 100.
    t.pencolor( colors[ x % 4] )    # Cycles through the pen colors.
    t.penup()                       # Lifts the pen so it won't draw while moving.
    t.forward( x * 4 )              # Move the pen forward the value of x times 4.
    t.pendown()                     # Puts the pen down so it can draw.
    
    # Writes the user's name using bold Arial font sized the value of x plus 4 divided by 4.
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    
    t.left(92)                      # Move the pen left by 92 degrees.
