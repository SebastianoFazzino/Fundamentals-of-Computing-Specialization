#Given the program template below, write a Python function print_goodbye() that defines a local variable message whose value is "Goodbye" 
#and prints the value of this local variable to the console. Note that the existing global variable message retains its original value "Hello" after the call to print_goodbye() completes.

def print_goodbye():
    message = "Goodbye"
    print(message)


message = "Hello"
print (message)
print_goodbye()
print (message)

message = "Ciao"
print (message)
print_goodbye()
print (message)




#Given the program template below, write a Python function set_goodbye() that updates a global variable message with the value "Goodbye" and prints the value of this global variable to the console. 
#Note that the existing global variable message has its original value "Hello" modified to "Goodbye" during the call to set_goodbye().

def set_goodbye():
    global message
    message = "Goodbye"
    print(message)
    

message = "Hello"
print (message)
set_goodbye()
print (message)

message = "Ciao"
print (message)
set_goodbye()
print (message)





#Given the program template below, implement four functions that manipulate a global variable count as follows. 
#The function reset() sets the value of count to be zero, the function increment() adds one to count, 
#the function decrement() subtracts one from count, and the function print_count() that prints the value of count to the console.

def reset():
    global count
    count = 0
    
def increment():
    global count
    count += 1
    
def decrement():
    global count
    count -= 1
    
def print_count():
    print(count)

reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()




#Complete the program template below so that the resulting CodeSkulptor program opens a frame of size 100×200 with the title "My first frame". 
#You will need to add only two extra lines of code.

import simpleguitk as simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    print (message)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

frame.start()




#Given the program template below, modify the program to create a CodeSkulptor frame that opens a 200×100 pixel frame with the title "My second frame". 

message = "My second frame!"

# Handler for mouse click
def click():
    print (message)

# Assign callbacks to event handlers
frame = simplegui.create_frame("My second frame", 200, 100)
frame.add_button("Click me", click)

# Start the frame animation
frame.start()