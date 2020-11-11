# Mini-project #6 - Blackjack

# We start importing the module we need for the project
import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
hidden = True
outcome = ""
outcome2 = ""
d_score = 0
p_score = 0
dealer_pos = [80, 140]
player_pos = [80, 455]


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    '''This class is used to build the deck of cards and to draw the cards on the canvas'''
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
  
# define hand class
class Hand:
    '''This class is used to determine which cards both the dealer and the player have and
    get_value() method is used to calculate the value of the cards'''
    
    def __init__(self):
        self.hand = []
        
    def __str__(self): 
        s = "Hands contain "
        for card in self.hand:
            s += str(card)
            s += " "
        return s
    
    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def get_value(self):
        tot = 0
        for card in self.hand:
            rank = card.get_rank()
            value = VALUES[rank]
            tot += value
            if rank == 'A' and tot < 12:
                tot += 10                   
        return tot
       
    def draw(self, canvas, x_pos, y_pos):
        for card in self.hand:
            card.draw(canvas, [(x_pos + x_pos * self.hand.index(card)), y_pos])
            
 
        
# define deck class 
class Deck:
    '''Deck class is used to compose the cards deck that we need for playing blackjack'''
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        
    def shuffle(self):
        random.shuffle(self.deck)
        
        
    def deal_card(self):
        return self.deck.pop()
        
    def __str__(self):
        s = "Hands contain "
        for card in self.deck:
            s += str(card)
            s += " "
        return s 


#define event handlers for buttons
def deal():
    '''This function creates a deck object, it shuffles the cards in the deck and it assigns two cards per player'''
    global deck, player_hand, dealer_hand, in_play, d_score, outcome, outcome2, hidden
    
    if in_play:
        d_score += 1
        
    deck = Deck()
    player_hand, dealer_hand = Hand(), Hand()
    deck.shuffle()
    
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    hidden = True
    
    p_value = player_hand.get_value()
    if p_value == 21:
        outcome = "Player has 21"
    else:
        outcome = "Player has " + str(p_value) + ", hit or stand?"
    
    outcome2 = "Dealer waits..."
    in_play = True
    

def hit():
    '''When called, this function assigns one more card to the player hand and it calculates the total value of his cards'''
    global player_hand, in_play, p_score, d_score, outcome, outcome2, hidden

    if in_play:
        player_hand.add_card(deck.deal_card())
        outcome2 = "Dealer waits..."
        player_hand.get_value()
        if player_hand.get_value() < 21:
            outcome = "Player has " + str(player_hand.get_value()) + ", hit or stand?"
        if player_hand.get_value() == 21:
            outcome = "Player has 21"
        if player_hand.get_value() > 21:
            outcome = "Player busted!"
            outcome2 = "Dealer wins!"
            d_score += 1
            in_play = False
            hidden = False
        


def stand():
     """When called, this function calculates the value of the dealer's cards and if it's less than 18, it assigns more card to him.
     Then it compares the value of both players' cards and it determines who won the game"""
     global dealer_hand, in_play, p_score, d_score, outcome, outcome2, hidden
     hidden = False
     
     outcome = "Player has " + str(player_hand.get_value())
     outcome2 = "Dealer has " + str(dealer_hand.get_value())
     if in_play:
        dealer_hand.get_value()
        player_hand.get_value()
        if dealer_hand.get_value() == 21:
            outcome2 = "Dealer has 21"
            outcome = "Dealer wins!"
            d_score += 1
            in_play = False
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome2 = "Dealer has " + str(dealer_hand.get_value())
            outcome = "Dealer wins!"
            d_score += 1
            in_play = False
        if dealer_hand.get_value() >= 18 and dealer_hand.get_value() < player_hand.get_value():
            outcome2 = "Dealer has " + str(dealer_hand.get_value())
            outcome = "Player wins!"
            p_score += 1
            in_play = False
            
        while dealer_hand.get_value() < player_hand.get_value() and dealer_hand.get_value() < 21:
              dealer_hand.add_card(deck.deal_card())
              if dealer_hand.get_value() == 21:
                  outcome2 = "Dealer has 21"
                  outcome = "Dealer wins!"
                  d_score += 1
                  in_play = False
              if dealer_hand.get_value() < 21 and dealer_hand.get_value() >= player_hand.get_value():
                  outcome2 = "Dealer has " + str(dealer_hand.get_value())
                  outcome = "Dealer wins!"
                  d_score += 1
                  in_play = False
              elif dealer_hand.get_value() > 21:
                  outcome2 = "Dealer busted!"
                  outcome = "Player wins!"
                  in_play = False
                  p_score += 1
              


# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, dealer_pos[0], dealer_pos[1])
    player_hand.draw(canvas, player_pos[0], player_pos[1])
    canvas.draw_text(outcome, [70, 400], 20, "white")
    canvas.draw_text(outcome2, [70, 320], 20, "white")
    canvas.draw_text(("dealer score: " + str(d_score)), [485, 50], 18, "#EDFF21")
    canvas.draw_text(("player score: " + str(p_score)), [485, 580], 18, "#EDFF21")
    canvas.draw_text("Blackjack", [60, 90], 48, "#EDFF21")
    
    if hidden:
        canvas.draw_image(card_back, [CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [196, 188], CARD_SIZE)
    if not in_play:
        canvas.draw_text("New Deal?", [400, 360], 24, "#EDFF21")


# initialization frame
frame = simplegui.create_frame("Blackjack", 670, 600)
frame.set_canvas_background("#3F888F")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

