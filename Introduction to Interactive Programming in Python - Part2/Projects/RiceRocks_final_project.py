# This is the final version of RiceRocks that is inspired by the classic arcade game Asteroids

# Link to the project:  https://py3.codeskulptor.org/#user306_uCZ2U7c1i2_0.py

# we import the modules needed
import simplegui
import math
import random

# we create global variables
WIDTH = 900
HEIGHT = 650
TOT_WIDTH = 1200
score = 0
lives = 3
level = 1
best_score = 0
time = 0
FRICTION = 0.985
started = False
collision = False
game_over = False
rocks = set([])
missiles = set([])
explosions = set([])
life_group = set([])
max_asteroids = 5
target = 500
font = "monospace"

class ImageInfo:
    '''This class is used to store all sprites information'''
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
splash2_info = ImageInfo([125, 31], [250, 62])
splash2 = simplegui.load_image("https://dl.dropbox.com/s/ssimtkqqqxfpmej/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 60)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# extra life pick-up
life_info = ImageInfo([15, 12.5], [30, 25], 32, 360)
life_image = simplegui.load_image("https://dl.dropbox.com/s/oes048xkn0zpt4x/Heart.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.4)
ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/v91gnybd7ifuyin/ship_thrust_sound_2.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
life_sound = simplegui.load_sound("https://dl.dropbox.com/s/mlctm1l0nqtwbm8/Health.mp3")

# helper functions to handle transformations and game mechanics
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def num_asteroids():
    global max_asteroids
    max_asteroids = (score // 150) + 5
    return max_asteroids

def set_level():
    global level
    level = (score // 150) + 1
    return level

def update_best_score():
    global best_score
    if score > best_score:
        best_score = score
        return best_score
      
def soundtrack_handler():
    if started:
        soundtrack.play()
        soundtrack.set_volume(.6)
    if not started:
        soundtrack.set_volume(.1)

def set_game_over():
    global started, game_over, lives, score, rocks, life_group
    started = False
    game_over = True
    soundtrack_handler()
    lives = 3
    score = 0
    rocks = set([])
    life_group = set([])

def click(pos):
    global started, game_over, rocks, life_group
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started or game_over)  and inwidth and inheight:
        started = True
        game_over = False
        soundtrack_handler()
        rocks = set([])
        life_group = set([])

# Ship class
class Ship:
    '''The ship class is used to draw the spaceship on the canvas'''
    def __init__(self, pos, vel, angle, image, info, sound):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image 
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = sound
               
    def draw(self,canvas):
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]],
                              self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # we update velocity
        if self.thrust:
            forward = angle_to_vector(self.angle)
            self.vel[0] += forward[0] * 0.2
            self.vel[1] += forward[1] * 0.2
             
        # we apply friction
        self.vel[0] *= FRICTION
        self.vel[1] *= FRICTION
               
    def shoot(self):
        # this method creates a new missile every time the spacebar is pressed. The initial position of the missile
        # corresponds to the tip of the spaceship
        global missiles
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 5 * forward[0], self.vel[1] + 5 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missiles.update(set([a_missile]))
        
    def keydown(self, key):
        if started:
            self.key = key
            if self.key == simplegui.KEY_MAP["right"]:
                self.angle_vel += 0.12
            if self.key == simplegui.KEY_MAP["left"]:
                self.angle_vel -= 0.12
            if self.key == simplegui.KEY_MAP["up"]:
                self.thrust = True
                self.sound.play()
            if self.key == simplegui.KEY_MAP["space"]:
                self.shoot()
        else:
            pass
            
    def keyup(self, key):
        self.key = key
        if self.key == simplegui.KEY_MAP["right"]:
            self.angle_vel = 0
        if self.key == simplegui.KEY_MAP["left"]:
            self.angle_vel = 0
        if self.key == simplegui.KEY_MAP["up"]:
            self.thrust = False
            self.sound.pause()
            self.sound.rewind()
                   
# Sprite class
class Sprite:
    '''The sprite class is used for drawing asteroids and missiles on the canvas'''
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated and collision:
            i = self.age % 24
            center = [(self.image_center[0] +  i * self.image_size[0]), self.image_center[1]]
            canvas.draw_image(self.image, center, self.image_size, self.pos, self.image_size, self.angle) 
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        # we update sprites position and velocity
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        # we update sprites' age so that they are drawn on the canvas for a limited time
        self.age += 1
        if self.age >= self.lifespan:
            return True
           
    def collide(self, other_object):
        # this method is used to determine wether two objects collide
        if (dist(self.pos, other_object.pos) <= (self.radius + other_object.radius)):
            return True
        else:
            return False
        
# we define the helper function for drawing groups of sprites and determine collisions

def draw_group(group, canvas):
    '''This function helps us drawing groups of object on the canvas'''
    remove = set([])
    for element in group:
        element.draw(canvas)
        if element.update():
            remove.add(element)
            group.difference_update(remove)
            
def group_collide(group, other_object):
    '''This function is used to determine if the ship collides with a rock'''
    global collision
    remove = set([])
    for element in group:
        if element.collide(other_object):
            remove.add(element)
            group.difference_update(remove)
            explosion = Sprite(element.pos, [0,0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosions.add(explosion)
            explosion_sound.rewind()
            explosion_sound.play()
            collision = True
            return collision
        
def extra_life(group, other_object):
    '''This function add one extra life to the player's ship, every time he collects a heart'''
    remove = set([])
    for element in group:
        if element.collide(other_object):
            remove.add(element)
            group.difference_update(remove)
            return True
                   
def missile_and_rock_collide(group1, group2):
    '''This function determines if a missile and a rock collide'''
    remove = set([])
    for element in group1:
        if group_collide(group2, element):
            remove.add(element)
            group1.difference_update(remove)
            return True

def draw(canvas):
    global time, lives, score
    
    # we create an animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [TOT_WIDTH / 2, HEIGHT / 2], [TOT_WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
       
    # we draw the splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())       
    if started:
        # we draw the ship and groups of object on the canvas
        draw_group(rocks, canvas)
        draw_group(missiles, canvas)
        draw_group(explosions, canvas)
        draw_group(life_group, canvas)
        my_ship.draw(canvas)
        my_ship.update()
    
    # using a series of if statement, we increase the player's score and we assign/subtract lives
    if group_collide(rocks, my_ship):
        lives -= 1
        if lives == 0:
            set_game_over()
            
    if missile_and_rock_collide(missiles, rocks):
        score += 10
        
    if extra_life(life_group, my_ship):
        lives += 1
        life_sound.rewind()
        life_sound.play()
    
    
    # we draw the user's interface, were we visualize instruction, player's score, lives, level and best score
    canvas.draw_line([1050, 0], [1050, HEIGHT], 300, "Darkblue")
    
    if not started and not game_over:
        canvas.draw_text("RiceRocks is inspired by the classic ",[920, 45], 13, "#E1CC4F", font)
        canvas.draw_text("arcade game 'Asteroids' by Atari. ",[920, 60], 13, "#E1CC4F", font)
        canvas.draw_text("Click on RiceRocks image to start ",[920, 90], 13, "#E1CC4F", font)
        canvas.draw_text("Controls: ",[920, 120], 13, "#E1CC4F", font)
        canvas.draw_text("UP ARROW - acceletate",[920, 135], 13, "#E1CC4F", font)
        canvas.draw_text("LEFT/RIGHT ARROW - turn left/right",[920, 150], 13, "#E1CC4F", font)
        canvas.draw_text("SPACEBAR - shoot missile",[920, 165], 13, "#E1CC4F", font)
        canvas.draw_text("You gain 10 points every time you",[920, 195], 13, "#E1CC4F", font)
        canvas.draw_text("destroy an asteroid with a missile. ",[920, 210], 13, "#E1CC4F", font)
        canvas.draw_text("If an asteroid hits the spaceship",[920, 225], 13, "#E1CC4F", font)
        canvas.draw_text("you lose one life.",[920, 240], 13, "#E1CC4F", font)
        canvas.draw_text("Every 50 asteroids you destroy or",[920, 255], 13, "#E1CC4F", font)
        canvas.draw_text("if your lives go down to 1, a heart",[920, 270], 13, "#E1CC4F", font)        
        canvas.draw_text("icon will appear for few seconds.",[920, 285], 13, "#E1CC4F", font)
        canvas.draw_text("Collect it to increase your lives!",[920, 300], 13, "#E1CC4F", font)
        canvas.draw_text("The speed and the number of",[920, 330], 13, "#E1CC4F", font)
        canvas.draw_text("asteroids increase based on what",[920, 345], 13, "#E1CC4F", font)
        canvas.draw_text("level you currently are.",[920, 360], 13, "#E1CC4F", font)
        canvas.draw_text("This project has been realized by",[920, 450], 13, "white", font)
        canvas.draw_text("Sebastiano Fazzino as part of ",[920, 465], 13, "white", font)
        canvas.draw_text("'Introduction to Interactive ",[920, 490], 13, "white", font)
        canvas.draw_text(" Programming with Python' ",[920, 505], 13, "white", font)
        canvas.draw_text(" by Rice University",[920, 525], 13, "white", font)
        canvas.draw_text("Art assets created by Kim Lathrop",[920, 580], 13, "white", font)
    if started:
        canvas.draw_text("score", [950, 250], 30, "#E1CC4F", font) 
        canvas.draw_text(str(score), [950, 285], 30, "white", font) 
        canvas.draw_text("lives",[950, 320], 30, "#E1CC4F", font)
        canvas.draw_text(str(lives), [950, 355], 30, "white", font) 
        canvas.draw_text("level",[950, 390], 30, "#E1CC4F", font) 
        canvas.draw_text(str(level), [950, 425], 30, "white", font) 
        canvas.draw_text("personal best", [950, 460], 30, "#E1CC4F", font)
        canvas.draw_text(str(best_score), [950, 495], 30, "white", font) 
    if started or game_over:
        canvas.draw_image(splash2, splash2_info.center, splash2_info.size, [1047, 80], splash2_info.size)
    if game_over:
        canvas.draw_text("game over!", [940, 320], 42, "#E1CC4F", font)
        canvas.draw_text("personal best", [950, 460], 30, "#E1CC4F", font)
        canvas.draw_text(str(best_score), [950, 495], 30, "white", font)       

def keydown(key):
    '''Here we call my_ship keydown method'''
    my_ship.keydown(key)
        
def keyup(key):
    '''Here we call my_ship keyup method'''
    my_ship.keyup(key)
    
# timer handler that spawns a rock     
def rock_spawner():
    '''We create a new asteroid every second using a timer. Asteroids have initial random position, spin direction, velocity and angle
       The velocity and total number of asteroids displayed increase based on the player's level'''
    global rocks
    # we update level, best score and total number of asteroids every second 
    set_level()
    update_best_score()
    tot_asteroids = num_asteroids()
    random_pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    random_vel = random.choice(list(range(-1, 1))) + level / 4
    random_ang = random.choice(list(range(-1, 1)))
    random_ang_vel = random.choice(list(range(-2, 2))) * 0.075 
    # we create asteroids up to a maximum of 5 + actual level at the same time and we make sure they don't appear too close to the ship
    if len(rocks) < tot_asteroids and dist(random_pos, my_ship.pos) > 100:
        a_rock = Sprite(random_pos, [random_vel, random_vel], random_ang, random_ang_vel, asteroid_image, asteroid_info)
        rocks.update(set([a_rock]))

def life_spawner():
    '''Every time the player's lives go down to 1 or every 50 asteroids destroyed, an extra life
       icon appears on the canvas for a few seconds'''
    global life_group, target
    random_pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
    random_vel = random.choice(list(range(-1, 1))) + 2 * random.random()
    if lives == 1:
        if len(life_group) < 1:
            life = Sprite(random_pos, [random_vel, random_vel], 0, 0, life_image, life_info)
            life_group.update(set([life]))
    if score > 0 and score >= target:
        if len(life_group) < 1:
            life = Sprite(random_pos, [random_vel, random_vel], 0, 0, life_image, life_info)
            life_group.update(set([life]))
            target += 500
            
# we initialize frame
frame = simplegui.create_frame("Asteroids", TOT_WIDTH, HEIGHT)
#we initialize the ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_sound)

# we register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)
timer2 = simplegui.create_timer(1000.0, life_spawner)

# get things rolling
timer.start()
timer2.start()
frame.start()
