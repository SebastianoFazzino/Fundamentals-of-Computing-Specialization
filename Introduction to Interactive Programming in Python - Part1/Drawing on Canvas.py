#Drawing on the canvas

#we start importing simpleguitk
import simpleguitk as simplegui

#we define a draw handler
def draw(canvas): 
    '''this function will be registered in the frame and it will draw
    the string "Hello!" and a circle'''
#draw_text can take five arguments: the text itself, coordinates(as list),
#font-size, color and font-family
    canvas.draw_text("Hello!", [100,100], 24, "white")
#draw_circle takes five argumens: circle center, radius, line_width, line_color,
#fill_color = color
    canvas.draw_circle([100, 100], 4, 4, "Red")

#we crate a frame
frame = simplegui.create_frame("test", 300, 200)

#we register the draw handler 
frame.set_draw_handler(draw)

#we start the frame
frame.start()


# *******************************************************************************


#one more example:
    
def draw2(canvas):
    canvas.draw_circle([100, 100], 50, 2, "Red", "Pink")
    canvas.draw_circle([300, 300], 50, 2, "Red", "Pink")
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100, 300], 50, 2, "Green", "Lime")
    canvas.draw_circle([300, 100], 50, 2, "Green", "Lime")
#draw_line takes 4 arguments: point1, point2, line_width, line_color
    canvas.draw_line([100, 300],[300, 100], 2, "Black")
#to draw a poligon, we pass a list of list as coordinates, line_width, line_color, fill_color = color
    canvas.draw_polygon([[150, 150], [250, 150], [250, 250], [150, 250]], 2, 
          "Blue", "Aqua")
    canvas.draw_text("An example of drawing", [60, 385], 24, "Black")

    
# Create a frame and assign callbacks to event handlers
frame2 = simplegui.create_frame("Home", 400, 400)
frame2.set_draw_handler(draw2)
frame2.set_canvas_background("Yellow")


# Start the frame animation
frame2.start()






#let's drive a truck on the canvas using circles and lines

def draw3(canvas):
    canvas.draw_circle((90,200), 20, 10, "white")
    canvas.draw_circle((210,200), 20, 10, "white")
    canvas.draw_line((50, 180), (250, 180), 40, "red")
    canvas.draw_line((55, 170), (90, 120), 5, "red")
    canvas.draw_line((90, 120), (130, 120), 5, "red")
    canvas.draw_line((180, 108), (180, 160), 140, "red")
    
    
frame3 = simplegui.create_frame("sample", 300, 300)
frame3.set_draw_handler(draw)

frame3.start()
