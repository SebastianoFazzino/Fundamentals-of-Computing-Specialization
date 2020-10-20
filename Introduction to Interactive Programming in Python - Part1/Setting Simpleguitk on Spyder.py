#SimpleGUITk is a wrapper for the CodeSkulptor SimpleGUI API using TkInter. CodeSkulptor is a browser-based Python interpreter used in the online course “An Introduction to Interactive Programming in Python”.
#This wrapper makes it easier to work in the development environment of your choice while still being able to quickly test your implementation without using a web browser.

#in order to use simplegui on Spyder IDE, I had to first pip install it on anaconda prompt: pip install SimpleGUITk.
#Find more information about SimpleGUITk on this website: https://pypi.org/project/SimpleGUITk/


import simpleguitk as simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
