# Implement aPerson class which has the fields first_name, last_name and birth_year. 
# This class should include the methods: __init__ which takes strings for the two name fields and an integer for the year of birth,
# full_name returns the full name for a person as a string, which is the first name followed by a space, followed by the last name, 
# age which takes the current year as input and returns the age in years of the person (Don't worry about days and months here, just return the difference of the two years.), 
# and __str__ returns a string that includes the first name and last name of the person as well as their year of birth. 

# Implementation of Person class


# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    
    def age(self, current_year):
        return (current_year - self.birth_year)
    
    def __str__(self):
        return ("The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year))
        
    
###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

print(joe)
print(john)
print(stephen)
print(scott)

print(joe.age(2020))
print(scott.age(2020))
print(john.full_name())
print(stephen.full_name())





# Write a function average_age that takes a list of Person objects along with the current year and returns the average age of the people in the list. 
# Remember that average_age should only use the methods defined in the Person class. (The body of average_age should not access the fields in a Person object directly.) 

# Use of Person class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    
    def age(self, current_year):
        return (current_year - self.birth_year)
    
    def __str__(self):
        return ("The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year))
        
 
# implementation of average_age
def average_age(person_list, current_year):
    total_age = 0
    for person in person_list:
        total_age += person.age(current_year)
    return total_age / float(len(person_list))


###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

instructors = [joe, john, stephen, scott]
print(average_age(instructors, 2020))

instructors.pop()
print(average_age(instructors, 2020))





# Implement a Student class which has the fields person (Person object), password (string), and projects (list of strings). 
# (Note that class uses another class, just as in Blackjack.) This class should include the following methods:, __init__ which takes a person (specified as Person object) 
# and a password (specified as a string) and creates a Student object (the list of projects should be empty to start), get_name which returns the student's full name, 
# check_password which take a supplied password and returns a Boolean indicating whether the supplied password matches the student's created password, 
# get_projects which returns the list of the student's projects and, add_project(project_name) which adds the specified project to the student's list of projects. 
# Note that this last method does not check whether the project already exists in the list.

# Implementation of Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)



# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
 
    
###################################################
# Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print(joe_student.get_name())
print(joe_student.check_password("qwert"))
print(joe_student.check_password("TopSecret"))

print(joe_student.get_projects())
joe_student.add_project("Create practice exercises")
print(joe_student.get_projects())
joe_student.add_project("Implement Minecraft")
print(joe_student.get_projects())








# Write a function assign that takes a list of Student objects, a student full name, a password, and a project as parameters.
# This function should search the list of students for students whose name and password match the supplied information. 
# When a match is found, the function checks the student's current list of projects for the supplied project. 
# If the project does not already exist in the list, the function adds the project to the list. 
# Remember to use only methods for the Student class to manipulate Student objects.

# Use of the Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    
    def age(self, current_year):
        return (current_year - self.birth_year)
    
    def __str__(self):
        return ("The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year))
        

# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
                
# definition of function assign
def assign(students, name, pwd, project):
    for student in students:
        if student.get_name() == name and student.check_password(pwd):
            if student.get_projects().count(project) == 0:
                student.add_project(project)
    
     
###################################################
# Testing code

# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print(joe.get_projects())
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print(joe.get_projects())

print(john.get_projects())
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print(john.get_projects())
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print(john.get_projects())





# We now return to Memory. For this problem, your task is to initialize a game of Memory using the Tile class.
# Starting from the provided template, complete the implementation of the function new_game() that initializes our version of Memory. 
# In particular, create a list with two copies of the numbers in range(0, DISTINCT_TILES) and use random.shuffle to shuffle the list. 
# Then, use the initializer for the Tile class to create a horizontal row of 2 * DISTINCT_TILES tiles whose numbers are hidden. 
# Finally, implement a draw handler using the draw method for the Tile class that draw all 16 tiles on the canvas.

# Initialize a game of Memory using the Tile class


import simpleguitk as simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals
def new_game():
    global deck, state, turns
    list1 = list(range(DISTINCT_TILES))
    list2 = list(range(DISTINCT_TILES))
    cards_list = list1 + list2
    random.shuffle(cards_list)
    deck = [Tile(cards_list[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     
       
            
# draw handler
def draw(canvas):
    for tile in deck:
        tile.draw_tile(canvas)

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
    
    
###################################################
# Create a horizontal row of 16 Memory tile with numbers hidden








# Your next task is to build a simple version of Memory that exposes tiles in response to mouse clicks. 
# Using the provided template, add code to the mouse handler mouseclick() that exposes a tile in response to a mouse click on that tile. 
# This code should interact with a tile using only Tile class methods. 

# Build clickable version of Memory using the Tile class


# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals
def new_game():
    global deck, state, turns
    list1 = list(range(DISTINCT_TILES))
    list2 = list(range(DISTINCT_TILES))
    cards_list = list1 + list2
    random.shuffle(cards_list)
    deck = [Tile(cards_list[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  

# definition of a Tile class
class Tile:
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     
       
            
# draw handler
def draw(canvas):
    for tile in deck:
        tile.draw_tile(canvas)
        
        
# define event handlers
def mouseclick(pos):
    for tile in deck:
        if tile.is_selected(pos):
            tile.expose_tile()
            
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# get things rolling
new_game()
frame.start()

    
###################################################
# Clicking on tile should flip them once






# To finish our object-oriented implementation of Memory, complete the implementation of the function mouseclick() in the provided template based on the state logic described in the Memory video. 
# Again, your code should interact with the tiles only via Tile class methods. When done correctly, the code should express the logic of this function in surprisingly readable manner.


# Final version of Memory using the Tile class


# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

# helper function to initialize globals


def new_game():
    global deck, state, turns
    list1 = list(range(DISTINCT_TILES))
    list2 = list(range(DISTINCT_TILES))
    cards_list = list1 + list2
    random.shuffle(cards_list)
    deck = [Tile(cards_list[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  
    
    
# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     
        

# define event handlers
def mouseclick(pos):
    global state, turns, turn1_tile, turn2_tile
    
    for tile in deck:
        if tile.is_selected(pos):
            clicked_tile = tile
            
    if clicked_tile.is_exposed():
        return
    
    clicked_tile.expose_tile()
    
    # add state code here
    if state == 0:
        state = 1
        turn1_tile = clicked_tile
    elif state == 1:
        state = 2
        turn2_tile = clicked_tile
        turns += 1
    else:
        if turn1_tile.get_number() != turn2_tile.get_number():
            turn1_tile.hide_tile()
            turn2_tile.hide_tile()
        state = 1
        turn1_tile = clicked_tile

            
# draw handler
def draw(canvas):
    for tile in deck:
        tile.draw_tile(canvas)
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)


# get things rolling
new_game()
frame.start()
    
    
###################################################
# Final version of Memory


