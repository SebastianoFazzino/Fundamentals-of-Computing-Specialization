#Practice Exercises for Functions
#Solve each of the practice exercises below. Each problem includes three CodeSkulptor links: one for a template that you should use as a starting point for your solution, one to our solution to the exercise, and one to a tool that automatically checks your solution.




#Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in miles.

def miles_to_feet(miles):
    return (miles * 5280)



#Write a Python function total_seconds that takes a parameters hours, minutes and seconds and returns the total number of seconds for hours,
#minutes and seconds

def total_seconds(hours, minutes, seconds):
    return ((hours * 3600) + (minutes * 60) + seconds)




#Write a Python function rectangle_perimeter that takes two parameters width and height 
#corresponding to the lengths of the sides of a rectangle and returns the perimeter of the rectangle in inches.

def rectangle_perimeter(width, height):
    return ((width * 2) + (height * 2))




#Write a Python function rectangle_area that takes two parameters width and height corresponding to the lengths of the sides of a rectangle and returns the area of the rectangle in square inches.

def rectangle_area(width, height):
    return (width * height)





#Write a Python function circle_circumference that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the circumference of a circle with radiusradius in inches. 
#Do not use π = 3.14, instead use the math module to supply a higher-precision approximation to π. 

import math
Pi = math.pi

def circle_circumference(radius):
    return (2 * radius * Pi)
    
    
 
    
 
#Write a Python function circle_area that takes a single parameter radius corresponding to the radius of a circle in inches and returns the the area of a circle with radius in square inches. 
#Do not use π = 3.14, instead use the math module to supply a higher-precision approximation to π.
   
def circle_area(radius):
    return (radius * radius * Pi)




#Write a Python function future_value that takes three parameters present_value, annual_rate and years and returns the future value of present_value dollars invested at annual_rate percent interest, compounded annually for years.

def future_value(present_value, annual_rate, years):
    return (present_value * (1 + 0.01 *  annual_rate) ** years)





#Write a Python function name_tag that takes as input the parameters first_name and last_name (strings) and returns a string of the form "My name is % %." where the percents are the strings first_name and last_name. 

def name_tag(first_name, last_name):
    return ("My name is " + first_name + " " + last_name)





#Write a Python function name_and_age that takes as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." where the percents are the string forms of name and age. 

def name_and_age(name, age):
    return (name + " is " + str(age) + " years old.")




#Write a Python function point_distance that takes as the parameters x0, y0, x1, y1 and returns the distance between the points (x0,y0) and (x1,y1).

def point_distance(x0, y0, x1, y1):
    distance = math.sqrt(((x1 - x0)**2) +  ((y1 - y0)**2))
    return distance




#Write a Python function triangle_area that takes the parameters x0, y0, x1, y1, x2, y2 and returns the area of the triangle with vertices
# (x0, y0), (x1, y1), (x2, y2).
#(Hint: use the function point_distance as a helper function and apply Heron's formula.)

def triangle_area(x0, y0, x1, y1, x2, y2):
    #we first calculate a, b and c in the triangle
    a = (point_distance(x0, y0, x1, y1))
    b = (point_distance(x1, y1, x2, y2))
    c = (point_distance(x0, y0, x2, y2))
    # s is the semi-perimeter of the triangle
    s = (a + b + c) / 2
    #now we can use Heron's formula to calculate the area of the triangle
    Area = math.sqrt(s * (s - a) * (s -b) * (s -c))
    return Area
    




#Write a Python function print_digits that takes an integer number in the range [0,100)[0,100), i.e., at least 0, but less than 100. It prints the message "The tens digit is %, and the ones digit is %.", 
#where the percent signs should be replaced with the appropriate values. (Hint: Use the arithmetic operators for integer division // and remainder % to find the two digits. Note that this function should print the desired message, rather than returning it as a string.

def print_digits(number):
    return ("The tens digit is " + str(number // 10) + " and the ones digit is " + str(number % 10))






#Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket with a specific number combination and, if the number on the ticket matches the numbers generated in a random drawing, the player wins a massive jackpot. 
# Write a Python function powerball that takes no arguments and prints the message "Today’s numbers are %, %, %, %, and %. The Powerball number is %.". 
#The first five numbers should be random integers in the range [1,60)[1,60), i.e., at least 1, but less than 60. In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates. 
# The Powerball number is a random integer in the range [1,36)[1,36), i.e., at least 1 but less than 36. 
#Use the random module and the function random.randrange to generate the appropriate random numbers.Note that this function should print the desired message, rather than returning it as a string. 

import random

def powerball():
    numbers = []
    i = 0
    while i < 5:
        num = random.randrange(1,60)
        if num not in numbers:
            numbers.append(num)
            i += 1
        else:
            continue
    while i < 6:
        power_num = random.randrange(1,36)
        if power_num not in numbers:
            numbers.append(power_num)
            i += 1
        else:
            continue
    return numbers

print(powerball())
    





#BONUS: IMPLEMENTED POWERBALL FUNCTION

#I've implemented the powerball function so that it allows the player to input his 6 numbers, then it randomly generates 6 winning numbers
#and according to how many numbers has the player guessed, the function prints out a message.



def powerball():
        
    your_nums = []
    i = 0
#using a while loop, we get the player to input 6 numbers
    while i < 6:
       Nums = input("Enter your numbers here: ")
       if int(Nums) not in your_nums:
          your_nums.append(int(Nums))
          i += 1
       else:
           continue
          
#we generate 6 random winning numbers  
    numbers = []
    i = 0
    while i < 5:
        num = random.randrange(1,60)
        if num not in numbers:
            numbers.append(num)
            i += 1
        else:
            continue
    while i < 6:
        power_num = random.randrange(1,36)
        if power_num not in numbers:
            numbers.append(power_num)
            i += 1
        else:
            continue
    #we print out the winning numbers
    print ("Winning numbers are: {},{},{},{},{}, Powerball number is: {}".format(numbers[0],
                                                                                 numbers[1],
                                                                                 numbers[2],
                                                                                 numbers[3],
                                                                                 numbers[4],
                                                                                 numbers[5]))
    
    
    #we check how many numbers has the player guessed
    guessed_nums = []
    for num in your_nums:
        if num in numbers:
            guessed_nums.append(num)
            
    print("You guessed", len(guessed_nums), "numbers!")
    
    
    if len(guessed_nums) <= 2:
        print("Bummer, you'll be luckier next time!")
    elif len(guessed_nums) >= 3 and len(guessed_nums) < 5:
        print("Wow! Not bad at all!!!")
    elif len(guessed_nums) == 5:
        print("Amazing! You almost did jackpot!!!")
    else:
        print("*****CONGRATULATIONS, YOU DID JACKPOT*****")
    
  
#we call the function
powerball()





























    