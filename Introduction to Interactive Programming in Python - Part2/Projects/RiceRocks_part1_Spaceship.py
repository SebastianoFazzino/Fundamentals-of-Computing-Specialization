# In this project I've been working on the creation of a simple version of 2D space game RiceRocks that is inspired by the classic arcade game Asteroids
# This is just a first template of the more complete game, which I'll develop later on. In this version of the game is possible to move the spaceship
# using left/right arrow, accelerate using up arrow and shoot a missile using spacebar.

# Art assets created by Kim Lathrop, may be freely re-used in non-commercial projects

# we import the modules needed
import simplegui
import math
import random

# we create global variables
WIDTH = 1000
HEIGHT = 700
score = 0
lives = 3
time = 0
FRICTION = 0.985
missile_shot = False

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

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.4)
ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/v91gnybd7ifuyin/ship_thrust_sound_2.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


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
            canvas.draw_image(self.image, [134, 45], self.image_size, self.pos, self.image_size, self.angle)

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
        global a_missile, missile_shot
        missile_shot = True
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 5 * forward[0], self.vel[1] + 5 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        
                  
    def keydown(self, key):
        self.key = key
        if self.key == simplegui.KEY_MAP["right"]:
            self.angle_vel += 0.15
        if self.key == simplegui.KEY_MAP["left"]:
            self.angle_vel -= 0.15
        if self.key == simplegui.KEY_MAP["up"]:
            self.thrust = True
            self.sound.play()
        if self.key == simplegui.KEY_MAP["space"]:
            self.shoot()
    
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
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        
def draw(canvas):
    global time
  
    # we create an animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # we draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if missile_shot:
        a_missile.draw(canvas)
    
    # we update ship and sprites
    my_ship.update()
    a_rock.update()
    if missile_shot:
        a_missile.update()
       
    # we visualize lives and score on the canvas
    canvas.draw_text("lives: " + str(lives), [25, 45], 36, "#F75E25")
    canvas.draw_text("score: " + str(score), [850, 45], 36, "#F75E25")
    
def keydown(key):
    '''Here we call my_ship keydown method'''
    my_ship.keydown(key)
        
def keyup(key):
    '''Here we call my_ship keyup method'''
    my_ship.keyup(key)
    
# timer handler that spawns a rock     
def rock_spawner():
    '''We create a new asteroid every second using a timer. Asteroids have initial random position, spin direction, velocity and angle'''
    global a_rock
    a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)], [random.choice(list(range(-2, 2))) + 0.1 * random.random(), random.choice(list(range(-2, 2))) + 0.1 * random.random()],
                    random.choice(list(range(-1, 1))), random.choice(list(range(-2, 2))) * 0.075, asteroid_image, asteroid_info)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_sound)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.075, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
