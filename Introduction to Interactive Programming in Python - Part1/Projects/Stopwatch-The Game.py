# template for "Stopwatch: The Game"

import simpleguitk as simplegui
# define global variables
time = 0
width = 150
attempts = 0
guesses = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    '''This function takes an integer representing tenths of seconds
    it formats it into minutes, seconds and tenths of seconds and returns a string'''
    dec = (time % 10)
    sec = (time  // 10) % 10
    dec_sec = (time // 100) % 6
    min = (time // 600) % 10
    return  str(min) + ":" + str(dec_sec) +str(sec) + "." + str(dec)
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    '''This function starts the timer when Start button is clicked'''
    timer.start()

def Stop():
    '''This function stops the timer when Stop button is cliked,
    it increases the number of attempts by 1 and if the time is
    a whole second when the timer stops, it assign one point to the player'''
    global time, attempts, guesses
    if timer.is_running() == True:
        timer.stop()
        if time > 0.0:
            attempts += 1
            if time % 10 == 0:
                guesses += 1
    
           
def Reset():
    '''This function reset the timer, number of attempts and guesses
    when Reset button is clicked'''
    global time, attempts, guesses
    timer.stop()
    time = 0
    attempts = 0
    guesses = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global time, guesses, attempts
    format_time = format(time)
    score = str(guesses) + "/" + str(attempts)
    canvas.draw_text(format_time, [100,100], 36, 'White')
    canvas.draw_text(score, [260, 25], 20, 'white')    
                      
#frame
frame = simplegui.create_frame("Stop Watch", 300, 300)

# register event handlers
frame.add_button("Start", Start, width)
frame.add_button("Stop", Stop, width)
frame.add_button("Reset", Reset, width)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
