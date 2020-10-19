# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

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
    

import random          

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
    

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



