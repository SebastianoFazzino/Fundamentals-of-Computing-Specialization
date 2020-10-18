#Write a Python function is_even that takes as input the parameter number (an integer) and returns True if number is even and False if number is odd. 
#Hint: Apply the remainder operator to n (i.e., number % 2) and compare to zero.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    


#Write a Python function is_cool that takes as input the string name and returns True if name is either"Joe", "John" 
#or "Stephen" and returns False otherwise. 

def is_cool(name):
    if name == "Joe" or name == "John" or name == "Stephen":
        return True
    else:
        return False
    
    
    

#Write a Python function is_lunchtime that takes as input the parameters hour (an integer in the range [1,12]) and is_am (a Boolean “flag” that represents whether the hour is before noon). 
#The function should return True when the input corresponds to 11am or 12pm (noon) and False otherwise. 

def is_lunchtime(hour, is_am):
    if (hour == 11 and is_am == 'am') or (hour == 12 and is_am == 'pm'):
        return True
    else:
        return False
    
    



#Write a Python function is_leap_year that take as input the parameter year and returns True if year (an integer) is a leap year according to the Gregorian calendar and False otherwise. 
#The Wikipedia entry for leap yearscontains a simple algorithmic rule for determining whether a year is a leap year. Your main task will be to translate this rule into Python.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    



#Write a Python function interval_intersect that takes parameters a, b, c, and d and returns True if the intervals [a,b] and [c,d] intersect and False otherwise. 
#While this test may seem tricky, the solution is actually very simple and consists of one line of Python code. (You may assume that a ≤ b and c c ≤ d.)    

def interval_intersect(a, b, c, d):
    return (c <= b) and (a <= d)





#Write a Python function name_and_age that take as input the parameters name (a string) and age (a number) and returns a string of the form "% is % years old." 
#where the percents are the string forms of name and age. The function should include an error check for the case whenage is less than zero. 
#In this case, the function should return the string "Error: Invalid age". 

def name_and_age(name, age):
    if age < 0:
        return ("Error: Invalid age")
    else:
        return ("{} is {} years old".format(name, age))
    
    



#Write a Python function print_digits that takes an integer number in the range [0,100] and prints the message "The tens digit is %, and the ones digit is %."
#where the percents should be replaced with the appropriate values. The function should include an error check for the case when number is negative or greater than or equal to 100. 
#In those cases, the function should instead print "Error: Input is not a two-digit number."

def print_digits(num):
    if num < 0 or num > 100:
        return ("Error: Input is not a two-digit number.")
    else:
        return ("The tens digit is {}, and the ones digit is {}.".format(num // 10, num % 10))
    
    
    



#Write a Python function name_lookup that takes a string first_name that corresponds to one of "Joe", "Scott", "John" or "Stephen") and then returns their corresponding last name
#"Warren", "Rixner", "Greiner", "Wong"). If first_name doesn't match any of those strings, return the string "Error: Not an instructor".

def name_lookup(first_name):
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return ("Error: Not an instructor")
    



#Pig Latin is a language game that involves altering words via a simple set of rules. Write a Python function pig_latin that takes a string word and applies the following rules to generate a new word in Pig Latin.
#If the first letter in word is a consonant, append the consonant plus "ay" to the end of the remainder of the word. 
#For example, pig_latin("pig") would return "igpay". If the first letter in word is a vowel, append "way" to the end of the word.
#For example, pig_latin("owl") returns "owlway". You can assume that word is in lower case.

vowels = ['a', 'e', 'i', 'o', 'u']
def pig_latin(word):
    first_letter = word[0]
    end_of_word = word[1:]
    
    if first_letter in vowels:
        return (word + "way")
    else:
        return (end_of_word + first_letter + "ay")
    
    



#Given numbers a, b, and c, the quadratic equation ax^2 + bx + c = 0 can have zero, one or two real solutions (i.e; values for x that satisfy the equation).
#The quadratic formula x = (-b +/- sq(b2 - 4ac) / 2a) can be used to compute these solutions.
#The expression b^2 - 4ac is the discriminant associated with the equation.
#If the discriminant is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions. 
#Write a Python function smaller_root that takes an input the numbers a, b and c and returns the smaller solution to this equation if one exists. If the equation has no real solution, print the message
#"Error: No real solutions" and simply return. Note that, in this case, the function will actually return the special Python value None.

import math
def smaller_root(a, b, c):
   discriminant = (b ** 2 - 4 * a * c)
   if discriminant < 0 or a == 0:
        print ("Error: No real solutions")
   else:
        discriminant_sqrt = math.sqrt(discriminant)
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)






