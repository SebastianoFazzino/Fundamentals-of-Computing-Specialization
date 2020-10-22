#we start importing the modules needed
import math
import random
import simpleguitk as simplegui

#we define the global variables
secret_number = int
number_of_guesses = 7
Range = 100

def new_game():
    global number_of_guesses
    '''this helper function gets invoked every time a new game starts, when the range changes from 100 to 1000 and viceversa,
    if the user input is not an int or if is a number out of range, if the user guesses the number or if he runs out of attempts'''
    print("\nNew game, range is from 0 to", Range)
    print("Number of remaining guesses is", number_of_guesses)
    


def range100():
    '''this function sets the secret_number range to 100, compute the number of attempts and invokes new_game function'''
    global secret_number, number_of_guesses, Range
    secret_number = random.randrange(0, 100)
    Range = 100
    #using the math module, we compute n guesses where n is the smallest integer such that 2 ** n >= high - low + 1
    #we use ceil() function to round up the number obtained and we calculate the logarithm of given range, base 2
    number_of_guesses = math.ceil(math.log(Range, 2))
    new_game()
    
    


def range1000():
    '''this function sets the secret_number range to 1000, compute the number of attempts and invokes new_game function'''
    global secret_number, number_of_guesses, Range
    secret_number = random.randrange(0, 1000)
    Range = 1000
    number_of_guesses = math.ceil(math.log(Range, 2))
    new_game()
    


def input_guess(guess):
    '''this function determines if the user input is a valid number and if not it restarts the game
    if the input is a valid number, it checks if it's the equal to the secret number, if not, it decrease the user 
    number of attempts left by 1. Once the user guesses the secret number or the number of attempts reaches 0, the game restarts'''
    global secret_number, number_of_guesses, Range
    
    try:
       your_guess = int(guess)
    
    
       if your_guess < 0 or your_guess > Range:
          print("\n*** Please enter a number between 0 and", Range, "***")
          range100()
       
       else:
        
           print("\nYour guess was:", your_guess)
    
           if your_guess > secret_number and number_of_guesses > 0:
              print("Lower!")
              number_of_guesses -= 1
              print("Number of remaining guesses is", number_of_guesses)
            
           if your_guess < secret_number and number_of_guesses > 0:
              print("Higher!")
              number_of_guesses -= 1
              print("Number of remaining guesses is", number_of_guesses)
            
           if your_guess == secret_number and number_of_guesses > 0:
              print("\n*** Correct! ***")
              range100()
            
           if number_of_guesses == 0:
              print("You ran out of guesses attempts!")
              print("*** Secret Number was:", secret_number, "***")
              range100()
    
    except:
        print("\n*** Incorrect Input! ***")
        range100()
      
    
    
#we create the frame, buttons and input 
frame = simplegui.create_frame("Guess the Number!", 200, 200)
frame.add_button("Range 0-100", range100, 150)
frame.add_button("Range 0-1000", range1000, 150)
frame.add_button("Start New Game", range100, 150)
frame.add_input("Enter your number here!", input_guess, 150)
    
#we invoke range100() and we start the frame
range100()
frame.start()

