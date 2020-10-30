import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw())
    
    def showHand(self):
        for card in self.hand:
            card.show()


card = Card("Spades", 6)
#card.show()

deck = Deck()
#deck.show()
deck.shuffle()
#deck.show()
draw_card = deck.draw()
#draw_card.show()

player = Player("hello")
player.draw(deck)
player.showHand()
