### Memory Game ###

import simpleguitk as simplegui
import random
import math

width = 800
height = 100

list1 = list(range(1, 9))
list2 = list(range(1, 9))
card_deck = list1 + list2
card_position = (width / 16)

card1 = 0
card2 = 0
state = 0
turns = 0

# helper function to initialize globals
def new_game():
    '''this funcion gets invoked any time a new game starts, it sets the parameters
    turns, state, exposed to their default values and shuffle the card deck'''
    global card_deck, exposed, turns
    random.shuffle(card_deck)
    turns = 0
    state = 0
    exposed = [False for i in range(16)]
    

# define event handlers
def mouseclick(pos):
    '''this funcion uses some logic to flip cards and compare cards value'''
    global exposed, card1, card2, state, turns
    
    i = math.floor(pos[0] / 50) 
          
    if exposed[i]:
        return
    if not exposed[i]: 
        if state == 0:
            state = 1
            exposed[i] = True
            card1 = i
                                    
        elif state == 1:
            state = 2
            exposed[i] = True 
            card2 = i 
            
        elif state == 2: 
            if card_deck[card1] != card_deck[card2]:
                exposed[card1] = False
                exposed[card2] = False
                state = 1   
                exposed[i] = True
                card1 = i
            
            if card_deck[card1] == card_deck[card2]:
                state = 1   
                card1 = i
                exposed[i] = True
                card2 = 0
            turns += 1
      

    
def draw(canvas):
    '''this funcion is used to draw the fron and back of the cards on the canvas'''
    global turns, exposed
    for i in range(len(card_deck)):
        if exposed[i]:
            canvas.draw_text(str(card_deck[i]), [(card_position * i + 15), 65], 48, "#256D7B")
        if not exposed[i]:
            canvas.draw_line([(card_position * i + 25), 0], [(card_position * i + 25), 100], 50, "#256D7B")
            canvas.draw_circle([(card_position * i + 20), 50], 4, 4, "Black", "Black")
            canvas.draw_circle([(card_position * i + 30), 50], 4, 4, "Black", "Black")
            canvas.draw_circle([(card_position * i + 25), 45], 4, 4, "Black", "Black")
            canvas.draw_circle([(card_position * i + 25), 55], 4, 4, "Black", "Black")
            
    # we draw lines to separate the cards   
    line_w = 0
    for i in range(17):
        canvas.draw_line([line_w, 0], [line_w, 100], 4, "Black")
        line_w += 50
    
    # a message pops up once the user has combined all the cards couples
    if exposed.count(True) ==  len(card_deck):
        canvas.draw_line([0,50], [800,50], 100, "White")
        canvas.draw_text("*** Congratulations!!! ***", [120, 70], 50, "#256D7B")
        
                
    #we set the label so thet it updates the number of turns    
    label.set_text("Turns = " + str(turns))
    
    
# we create frame and add a button and labels
frame = simplegui.create_frame("Memory", width, height)
frame.set_canvas_background("White")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# we register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# we get things rolling
new_game()
frame.start()

