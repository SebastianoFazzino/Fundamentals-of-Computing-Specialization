# SimpleGUI program template

# Import the module
import simpleguitk as simplegui

# Define global variables (program state)
counter = 0
# Define "helper" functions
def increment():
    global counter
    counter += 1
# Define event handler functions
def tick():
    increment()
    print (counter)

def press_button():
    global counter
    counter = 0
    
# Create a frame
frame = simplegui.create_frame("SimpleGUI Test", 100, 100)
# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", press_button)
# Start frame and timers
frame.start()
timer.start()

#this will initialize a timer and will create a frame with a 'click me!' button
#every time we clik the button, the timer will restart