# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.



# Up here, before everything else, we import the modules needed
import random
import time


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
    


        

# These lines runs your main function!
# You can change the questions if you wish.
# Only yes-or-no style questions will make sense.
#mystical_octosphere("Are the Cubs going to win the World Series?")

