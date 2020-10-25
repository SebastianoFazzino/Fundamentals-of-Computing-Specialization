# Counter ticks
#The following program should count upward from zero.
#Print the counter values 0, 1, 2, … to the console. 
#Add two lines of Python to make this program work. 
#Hint: Add a global variable to a timer callback, and start a timer.

import simpleguitk as simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print(counter)
    counter += 1
    
# create timer
timer = simplegui.create_timer(1000, tick)
# start timer
timer.start()





# Counter with buttons
#Given the solution from the following problem, we again want a counter printed to the console. 
#Add three buttons that start, stop and reset the counter, respectively.

counter = 0

# Timer handler
def tick():
    global counter
    print(counter)
    counter += 1
    
# Event handlers for buttons 
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global counter
    
    counter = 0
    timer.start()

        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start Timer", start, 150)
frame.add_button("Stop Timer", stop, 150)
frame.add_button("Reset Timer", reset, 150)
timer = simplegui.create_timer(1000, tick)


frame.start()







#Use a timer to toggle the canvas background back and forth between red and blue every 3 seconds. 
#Use the CodeSkulptor Docs to locate the appropriate call to change the background color of the canvas.


color = "Red"


# Timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    frame.set_canvas_background(color)
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()






# Expanding circle by timer
#Create a circle in the center of the canvas. 
#Use a timer to increase its radius one pixel every tenth of a second.


WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([100,100], radius, 2, "red", "yellow")
    
        
# Create frame and timer
frame = simplegui.create_frame("Circle", WIDTH, HEIGHT)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# Start timer
timer.start()
frame.start()




# Reflex tester

#Use a timer to measure how fast you can press a button twice. 
#Create a button that starts a timer that ticks every hundredth of a second. 
#The first button press starts the measurement. 
#The second button press ends the measurement. 
#Print to the console the time elapsed between button presses. 
#The next two button presses should repeat this process, making a new measurement. 
#Hint: We suggest that you keep track of whether the program is on the first 
#or second button press using a global Boolean variable.


total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global total_ticks, first_click
    if first_click:
        first_click = False
        total_ticks = 0
        timer.start()
    else:
        first_click = True
        timer.stop()
        print("Time between clicks is: " + str(total_ticks / 100))
        total_ticks = 0
            


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
