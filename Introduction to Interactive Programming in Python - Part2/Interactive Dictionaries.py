# This takes a message as input, it encodes or decodes it and gives another message as output
# To make it work, we're using a dictionary and its properties and random module 

# Cipher

import simpleguitk as simplegui
import random

CIPHER = {}

LETTERS = "abcdefghijklmnopqrstuvwxyz "

message = ""

def init():
    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    for ch in LETTERS:
        CIPHER[ch] = letter_list.pop()
    

# Encode button
def encode():
    '''This function encode the message we input'''
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print( message, "encodes to", emsg)

# Decode button
def decode():
    '''This function decode the message we input, looking for key values in CIPHER Dictionary'''
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print(message, "decodes to", dmsg)

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)


init()
# Start the frame animation
frame.start()
