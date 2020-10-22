# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

# ***************************************************************************************
# In this version of the mystical octosphere, I've implemeted a GUI interface that allows 
# the user to input a question and get back an answer on the console
# ***************************************************************************************

# Up here, before everything else, we import the modules needed
import random
import time
import simpleguitk as simplegui



def number_to_fortune(number):
    '''this helper function takes a number as input and returns an answer'''
    
    if number == 0:
        return "Yes, for Sure!"
    if number == 1:
        return "Probably yes."
    if number == 2:
        return "Seems like yes..."
    if number == 3:
        return "Definitely not!"
    if number == 4:
        return "Probably not."
    if number == 5:
        return "I really doubt it..."
    if number == 6:
        return "Not sure, check back later!"
    if number == 7:
        return "I really can't tell"
    else:
        return "Please enter a number between 0 and 7!"    

    

def mystical_octosphere(question):
    '''this function takes a question as input, random generates a number,
    and deoending what number it generates, it return an answer'''
    print(question)
     #we use time.sleep to generate some sunspence
    time.sleep(1.5)
    print("You shake the mystical octosphere.")
    
    #we random generate a number between 0 and 7
    answer_number = random.randrange(0,8) 
    #using number_to_fortune function, we convert the number generated into an answer
    answer_fortune = number_to_fortune(answer_number)  
    
    time.sleep(1.5)
    print("The cloudy liquid swirls, and a reply comes into view...")
    
    time.sleep(1.5)
    print("The mystical octosphere says...")
   
    print("\n", "*** " + answer_fortune + " ***", "\n")
    
   
 
#we define one more function that calles the previously deifned 'mystical octosphere' function   
def question_input(question):
    return mystical_octosphere(question)


    
#we create a frame object
frame = simplegui.create_frame("Mystical Octosphere", 100, 50)
frame.add_input("Type tour question here!", question_input, 150)

#we visualize the frame
frame.start()
    


        



