#Modify the following program template to print "It works!" on the canvas.
import simpleguitk as simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
#frame = simplegui.create_frame("It works", 400, 200)
#frame.set_draw_handler(draw)

#frame.start()




#Given the following program template, add draw commands to the draw handler to draw "This is easy?" on the canvas. 
#The precise size and location of the text on the canvas is not important.


# Draw handler
def draw2(canvas):
    canvas.draw_text("This is easy?", [75, 120], 36, "yellow")
    

# Create frame and assign callbacks to event handlers
#frame2 = simplegui.create_frame("This is easy", 400, 200)
#frame2.set_draw_handler(draw2)


# Start the frame animation
#frame2.start()




#Create a canvas of size 96×96, and draw the letter "X" with font size 48 in the upper left portion of the canvas. 
#Review the syntax for the SimpleGUI method draw_text and the layout of canvas coordinates.

def draw3(canvas):
    canvas.draw_text("X", [0,60], 48, "red")
    
#frame3 = simplegui.create_frame("X letter", 96, 96)
#frame3.set_draw_handler(draw3)

#frame3.start()




#Write a function format_time that takes an integer number of seconds in range(0, 3600) and converts it into string 
#that states the number of minutes and seconds. Remember to use the operations // and %. (Note that this example requires no interactive code.) 


def format_time(Int):
    minutes = Int // 60
    seconds = Int % 60
    return(str(minutes) + " minutes and " + str(seconds) + " seconds.")

#test

print(format_time(23))
print(format_time(1237))
print(format_time(0))
print(format_time(1860))





#Complete the program template below and add two buttons that control the radius of a white ball centered in the middle of the canvas. 
#Clicking the “Increase radius” button should increase the radius of the ball. Clicking the “Decrease radius” button should decrease the radius of the ball, 
#except that the ball radius should always be positive.

#we define the global variables
height = 400
width = 400
radius = 20
radius_increment = 10
border = 2
border_increment = 1
circle_color = "White"

#draw handler
def draw4(canvas):
    canvas.draw_circle([width // 2, height // 2], radius, border, "red", circle_color)

#helper functions
def increase():
    global radius, border
    radius += radius_increment
    border += border_increment
        
def decrease():
    global radius, border
    radius -= radius_increment
    border -= border_increment
    
def custom_radius(r):
    global radius
    radius = int(r)
    
def custom_border(b):
    global border
    border = int(b)
    
def custom_color(c):
    global circle_color
    circle_color = c
    
 
#we create the frame
frame4 = simplegui.create_frame("The Circle!", 400, 400)
frame4.set_draw_handler(draw4)
frame4.add_button("Increase", increase, 150)
frame4.add_button("Decrease", decrease, 150)
frame4.add_input("Customize Radius", custom_radius, 150)
frame4.add_input("Customize Border", custom_border, 150)
frame4.add_input("Customize Color", custom_color, 150)

#we visualize the frame
frame4.start()




















