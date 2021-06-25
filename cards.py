import random


# a card object has a number and a suit
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.name = '{} of {}'.format(number, suit)

# the deck contains all the cards and can act as a "dealer"
class Deck:
    
    def __init__(self):
        self.cards = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.numbers = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen','King','Ace']
        self.build_deck()
  
    def build_deck(self):
        print('Building the deck...')
        #self.cards.clear() # not available until python 3.3
        del self.cards[:]
    
        for suit in self.suits:
            for number in self.numbers:
                self.cards.append(Card(suit, number))
    
    def shuffle(self):
        print('Shuffling the cards...')
        random.shuffle(self.cards)
           
    def reset_deck(self):
        #self.cards.clear()
        del self.cards[:]
        self.build_deck()        
        self.shuffle()
        
    def deal_a_card(self):
        card = self.cards.pop(0)
        print('Drew a {} of {}'.format(card.number, card.suit))
        return card
    
    def draw_cards(self, number_of_cards):
        n=0
        while n < number_of_cards:
            card = self.cards.pop(0)
            print('Drew a {} of {}'.format(card.number, card.suit))
            n = n + 1
    
    def count_cards(self):
        card = self.cards[0]
        print('There are {} cards in the deck\n'.format(len(self.cards)))    
       
    def show_all_cards(self):
        print('showing all cards in the deck:\n')
        
        for card in self.cards:
            print('{} of {}'.format(card.number, card.suit))    
            
# A player has a name and a hand which holds cards (add credits eventually)
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card(self, card_object):
        self.hand.append(card_object)
    
    def remove_card(self, index=0):
        card = self.hand.pop(index)
        return card
    
    def show_hand(self):
        hand = [card.name for card in self.hand]
        print('PLAYER {} has '.format(self.name) + ', '.join(hand))
        return self.hand
    
    def drop_hand(self):
        #self.hand.clear()
        del self.hand[:]
        return self.hand
    
    
if __name__ == "__main__":
   
    my_deck = Deck()
    my_deck.shuffle()
    my_deck.deal_a_card()
    my_deck.deal_a_card()
    #my_deck.show_all_cards()
    my_deck.count_cards()
    p1 = Player('Josh')