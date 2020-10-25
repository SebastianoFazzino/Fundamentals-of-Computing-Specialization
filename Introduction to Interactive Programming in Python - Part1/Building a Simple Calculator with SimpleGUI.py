# calculator with all buttons

import simpleguitk as simplegui


# intialize globals

store = 0
operand = 0

# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print("Store = ", store)
    print("Operand = ", operand)
    print("")
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()
    
def clear():
    """reset store and operand values"""
    global store, operand
    store = 0
    operand = 0
    output()

def enter(num):
    """ enter a new operand"""
    global operand
    try:
       operand = float(num)
       output()
    except:
        print("Input must be a number!")
        
def draw(canvas):
    canvas.draw_text(["store:", store], [100, 100], 36, "White")
    canvas.draw_text(["operand:", operand], [100, 200], 36, "White")



# create frame
f = simplegui.create_frame("Calculator",500,300)

width = 120
# register event handlers
f.add_button("Print", output, width)
f.add_button("Swap", swap, width)
f.add_button("Add", add, width)
f.add_button("Sub", sub, width)
f.add_button("Mult", mult, width)
f.add_button("Div", div, width)
f.add_button("Clear", clear, width)
f.add_input("Input", enter, width)
f.set_draw_handler(draw)

# get frame rolling
f.start()
