class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    cards = []
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    numbers = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen','King','Ace']

    for suit in suits:
        for number in numbers:
            cards.append(Card(suit, number))
    
    
    def shuffle():
        print('shuffling the cards')
        
    def deal_a_card(self):
        card = self.cards[0]
        print('{},{}'.format(card.suit, card.number))
    
    def count_cards(self):
        card = self.cards[0]
        print('There are {} cards in the deck'.format(len(self.cards)))    
       
    def show_all_cards(self):
        for card in self.cards:
            print('{} of {}'.format(card.number, card.suit))    
        
my_deck = Deck()
#my_deck.deal_a_card()
my_deck.show_all_cards()
my_deck.count_cards()