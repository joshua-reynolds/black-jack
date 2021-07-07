import cards
import random
import time
import sys

# this makes the text appear at the proper time
# https://stackoverflow.com/questions/107705/disable-output-buffering
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)


class Dealer(cards.Deck): # inheritance
    def __init__(self):
        self.hand = []
        self.cards = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.numbers = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen','King','Ace']  
        self.reset_deck()
    
    def add_card(self, card_object):
        self.hand.append(card_object)    


    def show_first(self):
        hand = [card.name for card in self.hand]
        print('DEALER has ' +  hand[0])
        return self.hand     

    def show_hand(self):
        hand = [card.name for card in self.hand]
        print('DEALER has ' + ', '.join(hand))
        return self.hand 
    
    def deal_a_card(self):
        card = self.cards.pop(0)
        #print('Drew a {} of {}'.format(card.number, card.suit))
        return card    
 
class Player(cards.Player):  
    def __init__(self, name):
        self.name = name
        self.hand = []
        
        # for splitting
        self.hand_s1 = []
        self.hand_s2 = []
    
    def split_hand():
        if len(self.hand) == 2:
            self.hand_s1.append(self.hand[0])
            self.hand_s2.append(self.hand[1])
            return [self.hand_s1, self.hand_s2]

    
# something weird happens when a player has two aces, tally never goes past 12 
def tally_cards(hand):
    hand = [card.number for card in hand]
    faces = [10, 'Jack','Queen','King']
    
    can_split = False
    soft_hand = False
    
    tally = 0
    
    # if no cards in hand return 0, shouldn't happen
    if len(hand) == 0:
        print('ERROR: No cards in the hand')
        tally = 0
    
    # if two of the same cards are drawn, option to split becomes available
    if len(hand) ==  2:
        if hand[0] == hand[1]:
            can_split = True
    
    # replace face values with 10
    hand = [10 if card in faces else card for card in hand]
    
    # count aces
    number_of_aces = hand.count('Ace')
    
    
    # if there are three aces
    if number_of_aces == 4:

        if len(hand) == 4:
            tally = 14

        elif len(hand) > 4:
            hand = [card for card in hand if card != 'Ace']
            tally = sum(hand) + 14

            if tally > 21:
                tally = sum(hand) + 4     
    
    
    # if there are three aces
    elif number_of_aces == 3:

        if len(hand) == 3:
            tally = 13

        elif len(hand) > 3:
            #hand.remove('Ace')
            #hand.remove('Ace')
            #hand.remove('Ace')
            hand = [card for card in hand if card != 'Ace']
            tally = sum(hand) + 13

            if tally > 21:
                tally = sum(hand) + 3    
    
    
    # if there are two aces
    elif number_of_aces == 2:

        if len(hand) == 2:
            tally = 12
        
        elif len(hand) > 2:
            #hand.remove('Ace')
            #hand.remove('Ace')
            hand = [card for card in hand if card != 'Ace']
            tally = sum(hand) + 12
            
            if tally > 21:
                tally = sum(hand) + 2
    
    # if only one ace  
    elif number_of_aces == 1:
        
        hand.remove('Ace')
        
        if sum(hand) <= 10:
            soft_hand = True
            return [sum(hand) + 11, can_split, soft_hand]
        else:
            return [sum(hand) + 1, can_split, soft_hand] 
    else:
        hand = [10 if card in faces else card for card in hand]
        tally = sum(hand)
    
    return [tally, can_split, soft_hand]

if __name__ == "__main__":
    
    # create player and cards
    p = Player('Jim')
    c1 = cards.Card('Clubs','Ace')
    c2 = cards.Card('Spades','Ace')
    c3 = cards.Card('Hearts','Ace')
    c4 = cards.Card('Spades', 9)
    
    
    # add cards to player hand
    p.add_card(c1)  
    p.add_card(c2)
    p.add_card(c3)
    p.add_card(c4)
    
    # test tally
    p.show_hand() 
    print(tally_cards(p.hand))      