# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 800
HEIGHT = 500       
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 100
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT = True
LEFT = False
ball_pos = [(WIDTH / 2), (HEIGHT / 2)]
ball_vel = [0, 0]
paddle1_pos = [5, (HEIGHT / 2)]
paddle2_pos = [(WIDTH - 5), (HEIGHT / 2)]
paddle1_vel = 0
paddle2_vel = 0
target = 10
message = ""
color = ""

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def start():
    '''This function is used to initializa the game'''
    global score1, score2
    score1 = 0
    score2 = 0

def spawn_ball(direction):
    '''This function gets invoked every time a new game starts and it trows the ball
    at a random velocity and direction'''
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [(WIDTH / 2), (HEIGHT / 2)]
    
    random_velocity_right = [random.randrange(120, 240) / 40, random.randrange(60, 180) / 40]
    random_velocity_left = [- random.randrange(120, 240) / 40, - random.randrange(60, 180) / 40]
       
    if direction == RIGHT:
        ball_vel = random_velocity_right
    if direction == LEFT:
        ball_vel = random_velocity_left
    
# define event handlers
def new_game():
    '''This function resets score1, score2 and message and it random select a direction
    to pass as parameter in spawn_ball()'''
    global score1, score2, message
    score1 = 0
    score2 = 0
    message = ""
    target = 10
    random_direction = random.randrange(1,3)
    if random_direction == 2:
        spawn_ball(RIGHT)
    if random_direction == 1:
        spawn_ball(LEFT)
        
def stop_game():
    '''This function pauses the game'''
    global ball_pos, ball_vel
    ball_pos = [(WIDTH / 2), (HEIGHT / 2)]
    ball_vel = [0, 0]
    
def set_target(num):
    '''This function takes a number as input and set the target equals to that number.
    Default target is 10'''
    global target
    try:
        target =  int(num) 
    except:
        print("*** Target must be a number ***")
    
def draw(canvas):
    '''Here we draw all the main elements of the game and using some math, we determine collisions
    and motions of the ball'''
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, target, message, color
     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
                 
    # update ball
    ball_pos[0] += (ball_vel[0])
    ball_pos[1] += (ball_vel[1])
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white") 
     
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] -= paddle1_vel
    paddle2_pos[1] -= paddle2_vel
    
    if paddle1_pos[1] <= HALF_PAD_HEIGHT - 6:
        paddle1_pos[1] += 6
    if paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT + 6:
        paddle1_pos[1] -= 6
        
    if paddle2_pos[1] <= HALF_PAD_HEIGHT - 6:
        paddle2_pos[1] += 6
    if paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT + 6:
        paddle2_pos[1] -= 6
         
    # we draw paddles here
    canvas.draw_line([5, (paddle1_pos[1] - HALF_PAD_HEIGHT)],
                     [5, (paddle1_pos[1] + HALF_PAD_HEIGHT)], PAD_WIDTH, "#00F700")
    canvas.draw_line([795, (paddle2_pos[1] - HALF_PAD_HEIGHT)],
                     [795, (paddle2_pos[1] + HALF_PAD_HEIGHT)], PAD_WIDTH, "#EDFF21")
    
    # we determine whether paddle and ball collide
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
     
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (paddle1_pos[1] - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0] * 1.15
        else:
            score2 += 1
            spawn_ball(RIGHT)
                  
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        if (paddle2_pos[1] - HALF_PAD_HEIGHT) <= ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0] * 1.15    
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # we determine which player has won the game and we set a message accordingly
    if score1 == target:
        color = "#00F700"
        message = "PLAYER 1 WINS!!! "
        stop_game()
        
    if score2 == target:
        color = "#EDFF21"
        message = "PLAYER 2 WINS!!!"
        stop_game()     
                     
    # draw scores
    canvas.draw_text(str(score1), [360, 40], 40, "#00F700")
    canvas.draw_text(str(score2), [420, 40], 40, "#EDFF21")
    canvas.draw_text(message, [220, 200], 48, color)
    
     
def keydown(key):
    '''keydown() allows the players to move their paddles'''
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle1_vel = 0
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 6
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = -6
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 6
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = -6
         
def keyup(key):
    '''When a key is released, the paddle stops'''
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Classic Pong", WIDTH, HEIGHT)
frame.add_input("Set the target!", set_target, 150)
frame.add_button("START", new_game, 150)
frame.add_button("STOP", stop_game, 150)
frame.add_button("NEW GAME", new_game, 150)
frame.set_draw_handler(draw)
frame.set_canvas_background('#3B83BD')
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
start()
frame.start()

