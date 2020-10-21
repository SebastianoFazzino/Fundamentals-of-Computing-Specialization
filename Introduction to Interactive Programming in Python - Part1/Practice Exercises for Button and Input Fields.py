#First of all we import the modules we need for the exercises
import simpleguitk as simplegui
import random


#Write event handlers print_hello() and print_goodbye() for the two buttons with labels "Hello" and "Goodbye" 
#defined in the program template below. Pressing these buttons should print the messages "Hello" and "Goodbye", respectively, in the console.


Hello = "Hello"
Goodbye = "Goodbye"
width = 100

def hello():
    global Hello
    print(Hello)
    

def goodbye():
    global Goodbye
    print(Goodbye)
    

frame = simplegui.create_frame("Greetings", 200, 200)
frame.add_button("Hello", hello, width)
frame.add_button("Goodbye", goodbye, width)

frame.start()




#Given the three function print_color(), set_red(), set_blue() in the program template below, 
#create three buttons that print and manipulate the global variable color. 
#Use the CodeSkulptor Docs to determine the SimpleGUI method for creating a button if needed.

def set_red():
    global color
    color = "red"
    print(color)
    

def set_blue():
    global color
    color = "blue"
    print(color)

    
def print_color():
    print(color)
    
    
frame2 = simplegui.create_frame("Change Color", 200, 200)
frame2.add_button("RED", set_red, width)
frame2.add_button("BLUE", set_blue, width)
frame2.add_button("PRINT COLOR", print_color, width)

frame2.start()





#Given the program template below, implement four buttons that manipulate a global variable count as follows. 
#The function reset() sets the value of count to be zero, the function increment() adds one to \count, 
#the function decrement() subtracts one from count, and the function print_count() prints the value of count to the console. 

count = 0

def reset():
    global count
    count = 0
    print(count)

def increment():
    global count
    count += 1
    print(count)
    
def decrement():
    global count
    count -= 1
    print(count)
    
def print_count():
    print(count)
    
    
frame3 = simplegui.create_frame("Count", 200, 200)
frame3.add_button("Increment", increment, width)
frame3.add_button("Decrement", decrement, width)
frame3.add_button("Reset Count", reset, width)
frame3.add_button("Print Count", print_count, width)

frame3.start()




#Write a program that creates an input field and echoes input to that field to the console. 

def Input(inp):
    print(inp)
    
frame4 = simplegui.create_frame("Simple Input", 200, 200)
frame4.add_input("Input", Input, width)

frame4.start()




#Write a program allows a user to enter a word in an input field, translates that word into Pig Latin and prints this translation in the console. 
#For the sake of modularity, we suggest that you build a helper function that handles all of the details of translating a word to Pig Latin (see the practice exercises for logic and conditionals) . 
#The provided template includes the operations for extracting the first letter and rest- of the input word in the partial definition of this function. 

vowels = ["a", "e", "i", "o", "u"]

def pig_latin(word):
    first_letter = word[0]
    end_of_word = word[1:]
    
    if first_letter in vowels:
        return (word + "way")
    else:
        return (end_of_word + first_letter + "ay")
    
    
def get_input(inp):
    print(pig_latin(inp))
   
    
frame5 = simplegui.create_frame("Word-to-PigLatin", 200, 200)
frame5.add_input("Enter Word", get_input, width)

frame5.start()    
    
    
    
  
    
  
    
# Add an interactive user interface for your implementation of "Rock-paper-scissors-lizard-Spock". 
#Create an input field that takes a player's guess, generates a random computer guess, and prints out the player and computer choices as well as who won in the console. 
#Make sure that your program checks for and correctly responds to bad input.
    
    

def name_to_number(name):
    """This function takes a string as input and returns a number"""
    if name == "rock":
        return(0)
    if name == "Spock":
        return(1)
    if name == "paper":
        return(2)
    if name == "lizard":
        return(3)
    if name == "scissors":
        return(4)
    else:
        return("Invalid Input...")
    


def number_to_name(number):
    """"This function takes a number as input and returns a string"""
    if number == 0:
        return("rock")
    if number == 1:
        return("Spock")
    if number == 2:
        return("paper")
    if number == 3:
        return("lizard")
    if number == 4:
        return("scissors")
    else:
        return("Invalid Input...")
    


def rpsls(player_choice):  
    """This function will generate the computer choice, print out both player's and computer's choice
       and determine who between of the two won the game, or if we have a tie in case both choices are equal"""
       
    print("\n")
    
    print("Player chooses", player_choice)   
    player_number = name_to_number(player_choice)
   
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice)
    
    #We compute difference of comp_number and player_number modulo five
    if (comp_number - player_number) % 5 == 0:
        print("Player and computer tie!")
    if (comp_number - player_number) % 5 == 1 or (comp_number - player_number) % 5 == 2:
        print("Computer wins!")
    if (comp_number - player_number) % 5 == 3 or (comp_number - player_number) % 5 == 4:
        print("Player wins!")
  
    
def choice(inp):
    return(rpsls(inp))

    

frame6 = simplegui.create_frame("rock-paper-scissors-lizard-Spock Game", 200, 200)
frame6.add_input("Choice your sign", choice, width)

frame6.start()