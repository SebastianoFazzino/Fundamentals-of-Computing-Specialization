# For each mouse click, print the position of the mouse click to the console. 

import simpleguitk as simplegui
import math

# Echo mouse click in console

def click(pos):
    print("Mouse click at: " + str(pos))

frame = simplegui.create_frame("Mouse Click", 400, 400)
frame.set_mouseclick_handler(click)
frame.start()




# Modify the program template below so that clicking inside any of the three displayed circles prints the color of the clicked circle to the console. 
# Hint: Use the supplied function dist to compute the distance between the center of each circle and the mouse click.

# Circle clicking problem

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    if dist(pos, RED_POS) < RADIUS:
        print("You clicked on the Red Circle")
    if dist(pos, GREEN_POS) < RADIUS:
        print("You clicked on the Green Circle")
    if dist(pos, BLUE_POS) < RADIUS:
        print("You clicked on the Blue Circle") 
    if dist(pos, RED_POS) > RADIUS and \
       dist(pos, GREEN_POS) > RADIUS and \
       dist(pos, BLUE_POS) > RADIUS:
            print("You clicked on the canvas!")

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()





# Write a function day_to_number(day) that takes the supplied global list day_list and returns the position of the given day in that list.
# You can either use the Docs to locate the appropriate list method or write a for loop to implement this function.

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    for i in day:
        return day_list.index(day) + 1

    
# alternatively:
def day_to_number2(day):
    pos = 0
    for i in range(len(day_list)):
        if day_list[i] == day:
            pos = i
    return pos




# Write a function string_list_join(string_list) that takes a list of strings as input and returns a single string that is the concatenation of the strings in the list. 
# We recommend using a for loop to implement this function.

def string_list_join(string_list):
    new_string = ""
    for elements in string_list:
        new_string += elements
    return new_string





# Complete the given program template to produce a program that fills the canvas with a 10x10 grid of touching balls of the given size. 
# You should use two for loops, one nested inside the other, placed in the draw handler.

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
                               # circles coordinates
            canvas.draw_circle([2 * BALL_RADIUS * i + BALL_RADIUS, 2 * BALL_RADIUS *j + BALL_RADIUS], 
                               BALL_RADIUS, 3, "White", "Lightblue")
       
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()




# Write a program that draws a polyline (an open polygon) based on a sequence of mouse clicks. 
# The first click should create a point. Subsequent clicks should add a new segment to the polyline. 
#You should include a “Clear” button that deletes the polyline and restarts the drawing process.

import random

polyline = []
color = ""

# helper function
def random_color():
    global color
    num = random.randrange(0, 7)
    if num == 0:
        color = "Yellow"
    if num == 1:
        color = "Blue"
    if num == 2:
        color = "Orange"
    if num == 3:
        color = "Purple"
    if num == 4:
        color = "Lightgreen"
    if num == 5:
        color = "Darkgreen"
    if num == 6:
        color = "Red"
        
    return color


# define mouseclick handler
def click(pos):
    polyline.append(pos)
    random_color()
             
# button to clear canvas
def clear():
    global polyline
    polyline = []
    
# define draw
def draw(canvas):
    if len(polyline) > 0:
        canvas.draw_circle(polyline[0], 4, 3, "red")
        canvas.draw_polyline(polyline, 4, color)
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 500, 400)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()







