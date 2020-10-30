# Create a dictionary day_to_number that converts the days of the week "Sunday", "Monday", … into the numbers 0, 1, …, respectively.

day_to_number = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

# Test data

print(day_to_number["Sunday"])
print(day_to_number["Monday"])
print(day_to_number["Tuesday"])
print(day_to_number["Wednesday"])
print(day_to_number["Thursday"])
print(day_to_number["Friday"])
print(day_to_number["Saturday"])





# Create dictionary for name_lookup that, when you lookup the keys "Joe", "Scott", "John", and "Stephen", 
# you get the values "Warren", "Rixner", "Greiner", and "Wong", respectively.


name_lookup = {"Joe" : "Warren", "Scott" : "Rixner", "John" : "Greiner", "Stephen" : "Wong"}

# Test data

print(name_lookup["Joe"])
print(name_lookup["Scott"])
print(name_lookup["John"])
print(name_lookup["Stephen"])








# Debug the program template below so that the resulting program draws the supplied image on the canvas.

import simpleguitk as simplegui

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] // 2, test_image_size[1] // 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw)

# start frame
frame.start()






# Load this asteroid image ("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
# and draw the image centered at the last mouse click. Prior to any mouse clicks, the image should be drawn in the middle of the canvas. The image size is 95×93 pixels.


        
# global constants
WIDTH = 400
HEIGHT = 300
center = [WIDTH / 2, HEIGHT / 2]

# load test image
img = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
img_size = [95, 93]
img_pos = [img_size[0] //2, img_size[1] // 2]

# mouseclick handler
def click(pos):
    global center
    center = list(pos)    

    
# draw handler
def draw(canvas):
    canvas.draw_image(img, img_pos, img_size, center, img_size)

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()







# Find an image of your choosing, and upload it to an image sharing site such as imgur.com. 
# Add a direct link to the image to a CodeSkulptor program and write a program that draws the image on the canvas.


size = [640, 360]
center = [size[0] /2, size[1] / 2]

img = simplegui.load_image("https://media.2oceansvibe.com/wp-content/uploads/2015/02/ferrari3.jpg")


def draw(canvas):
    canvas.draw_image(img, center, size, center, [size[0] / 1.5, size[1] / 1.5])
      
    
frame = simplegui.create_frame("Ferrari", size[0], size[1])
frame.set_draw_handler(draw)

frame.start()