# Simple "screensaver" program.

# Import modules
import simpleguitk as simplegui
import random

# Global state
message = "Python is Fun!"
position = [100, 100]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text

    
# Handler for timer
def tick():
    global position
    x = random.randrange(0, 500)
    y = random.randrange(0, 500)
    position = [x, y]


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
# We create the timer here
timer = simplegui.create_timer(2000, tick)

# Start the frame animation
frame.start()
timer.start()

