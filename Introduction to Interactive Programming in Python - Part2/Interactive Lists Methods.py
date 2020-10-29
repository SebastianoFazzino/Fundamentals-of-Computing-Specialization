# Simple task list

import simpleguitk as simplegui
import math
import random

tasks = []

# Handler for button
def clear():
    global tasks
    tasks = []
    
# Handler for new task
def new(task):
    tasks.append(task)
    
# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)

# Handler for remove name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)
    
# Handler to draw on canvas
def draw(canvas):
    n = 1
    for task in tasks:
        pos = 30 * n
        canvas.draw_text(str(n) + ": " + task, [5, pos], 24, "White")
        n += 1
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()



# Using the list ball_list, we'll create a new circle
# every time we click on the canvas

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    ball_list.append(pos)


def draw(canvas):
    for ball_pos in ball_list:
        canvas.draw_circle(ball_pos, ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    



# In this other example, we create a new circle every time we clickon the canvas. 
# The circle color is randomly selected and it changes if we click over an existing circle


# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
color = ""

# helper functions
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def random_color(num):
    global color
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

# define event handler for mouse click, draw
def click(pos):
    color_select = random.randrange(0,7)
    
    # here we use the flag 'changed'
    changed = False
    
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = random_color(color_select)
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], random_color(color_select)])

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball[2])
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    



# in the following example, we create a new circle every time we click on the canvas
# and if we click on an exisiting cirle, it gets deleted.
# To do so we use list's method pop()

## intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# define event handler for mouse click, draw
def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

