import cards
import random
import time

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
 
    
    
def tally_cards(hand):
    hand = [card.number for card in hand]
    faces = [10, 'Jack','Queen','King']
    
    can_split = False
    soft_hand = False
    
    # if no cards in hand return 0, shouldn't happen
    if len(hand) == 0:
        return 0
    
    # if two of the same cards are drawn, option to split becomes available
    if len(hand) ==  2:
        if hand[0] == hand[1]:
            can_split = True
    
    # replace face values with 10
    hand = [10 if card in faces else card for card in hand]
    
    # count aces
    number_of_aces = hand.count('Ace')
    
    # if there are two aces
    if number_of_aces == 2:
        return [12, can_split, soft_hand]
    
    # if only one ace  
    if number_of_aces == 1:
        
        hand.remove('Ace')
        
        if sum(hand) <= 10:
            soft_hand = True
            return [sum(hand) + 11, can_split, soft_hand]
        else:
            return [sum(hand) + 1, can_split, soft_hand] 
    else:
        hand = [10 if card in faces else card for card in hand]
        return [sum(hand), can_split, soft_hand]

if __name__ == "__main__":
    
    game_status = 0
    
    ## test tally
    #deck = Dealer()
    #deck.shuffle()
    #hand = [deck.deal_a_card(), deck.deal_a_card(), deck.deal_a_card()]
    #results = tally_cards(hand)
    #print(results)
    
    
    while game_status == 0:
        
        # create entities
        dealer = Dealer()    
        players = [cards.Player("Josh"), cards.Player("Brenda"), cards.Player("Wiz Khalifa")]
        
        winners = []
        losers = []
        
        # deal first card
        print('Dealing first card...')
        for player in players:
            player.add_card(dealer.deal_a_card())
        
        dealer.add_card(dealer.deal_a_card())
        
        # deal second card 
        print('Dealing second card...\n')
        for player in players:
            player.add_card(dealer.deal_a_card())
        
        dealer.add_card(dealer.deal_a_card())
        
        # show dealers first card
        dealer.show_first()
        
        # if dealer has an ace, offer insurance
        print('\n')       
        
        # play the game
        for player in players:
            player.show_hand()
            results = tally_cards(player.hand)
            print(results)   
            print('\n')
            
            stand = False
            while stand == False:

                if results[0] == 21:
                    print('PLAYER {} has 21!'.format(player.name))
                    stand = True
                
                else:
                    choice = input('(H)it or (S)tand:')
                    
                    if choice == 'h':
                        player.add_card(dealer.deal_a_card())
                        player.show_hand()
                        results = tally_cards(player.hand)
                        print(results[0])
                        print('\n') 
                        if results[0] > 21:
                            print('Sorry, {} busted!'.format(player.name))
                            stand = True
                    
                    elif choice == 's':
                        stand = True
                        
                    else:
                        print('invalid response')
                    
            print('\n')    
        
        # dealer now plays
        play_on_soft_17 = True
        dealer.show_hand()
        print(tally_cards(dealer.hand))
        print('\n') 
        
        stand = False        
        while stand == False:
            
            if play_on_soft_17 == True and tally_cards(dealer.hand)[0] == 17 and tally_cards(dealer.hand)[3] == True:
                    dealer.add_card(dealer.deal_a_card())
                    dealer.show_hand()
                    print(tally_cards(dealer.hand))
                    print('\n')            
                        
            elif tally_cards(dealer.hand)[0] < 17:
                dealer.add_card(dealer.deal_a_card())
                dealer.show_hand()
                print(tally_cards(dealer.hand))
                print('\n') 
                
            elif tally_cards(dealer.hand)[0] > 21:
                print('The dealer busted!')
                stand = True              
            
            elif tally_cards(dealer.hand)[0] >= 17:
                stand = True  
                
                
        
        game_status = 1