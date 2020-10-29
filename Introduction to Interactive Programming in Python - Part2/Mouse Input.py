# Example of mouse input

# we import the modules we need
import math
import simpleguitk as simplegui

# we define global variables
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) **2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "black", ball_color)


def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "green"
    else:
        ball_pos = list(pos)
        ball_color = "red"

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("white")

# register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

#start frame
frame.start()


