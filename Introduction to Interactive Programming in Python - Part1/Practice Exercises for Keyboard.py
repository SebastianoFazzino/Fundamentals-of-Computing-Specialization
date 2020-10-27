# The program template contains a program designed to echo the message "Pressed up arrow" or 
# "Pressed down arrow" whenever the appropriate key is pressed. Debug the program template and fix the program.

# Key board debugging - debug and fix the code below

import simpleguitk as simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Start the frame animation
frame.start()






# Complete the program template below so that each press of the up arrow increases the radius of the white ball centered in the middle of the canvas 
#by a small fixed amount and each press of the down arrow key decreases the radius of the ball by the same amount. Your added code should be placed in the keydown handler. 
# (Note that draw_circle will throw an error if the radius of the circle is decreased to zero or less.)

# Ball radius control - version 1

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
# Add code here to control ball_radius
    #here we make sure that the ball doesn't overflow the canvas margins
    if key == simplegui.KEY_MAP["up"] and ball_radius < (HEIGHT / 2 - 2):
        ball_radius += BALL_RADIUS_INC
    #we make sure that the ball radius is never a posiive number
    elif key == simplegui.KEY_MAP["down"] and ball_radius > 3:
        ball_radius -= BALL_RADIUS_INC
    

# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()













# Complete the program template so that the program displays "Space bar down" on the canvas while the space bar is held down and 
# "Space bar up" while the space bar is up. You will need to add code to both the keydown and keyup handlers.

# Space bar status

message = "Space bar up"

# Handlers for keydown and keyup
def keydown(key):
    global message
    # add code here
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar down"

def keyup(key):
    global message
    # add code here 
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar up"


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()





# Complete the program template below so that holding down the up arrow key increases the radius of the white ball
# centered in the middle of the canvas by a small fixed amount each frame. Releasing the up arrow key causes that growth to cease.
# You will need to add code to the keydown and keyup handlers as well as the draw handler.


# Ball radius control - version 2

WIDTH = 300
HEIGHT = 200
ball_radius = 10
ball_growth = 0
BALL_GROWTH_INC = 2

# Handlers for keydown and keyup
def keydown(key):
    global ball_growth, ball_radius
    # add code here
    if key == simplegui.KEY_MAP["up"]:
        ball_growth += BALL_GROWTH_INC
    #we make sure that if the ball touches the canvas borders,
    #its radius goes back to 10px
    if ball_radius > HEIGHT / 2 - 2:
        ball_radius = 10 

def keyup(key):
    global ball_growth
    # add code here
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = 0
    
# Handler to draw on canvas
def draw(canvas):
    global ball_radius
    # add code here
    ball_radius += ball_growth
    
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()