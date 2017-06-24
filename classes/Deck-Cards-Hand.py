import random

class Card:
    """Representation of a card as a string (suit+rank)"""
    def __init__(self, suit, rank):
        self.card = suit + str(rank)

    def __str__(self):  return self.card
    def __repr__(self): return str(self)

class Hand:
    """representation of a hand as a list of Card objects"""
    def __init__(self,list_of_cards):
        self.hand = list_of_cards

    def __str__(self):  return str(self.hand)
    def __repr__(self): return str(self)

class Deck:
    """Representation of a deck as a list of Card objects."""
    def __init__(self):
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','D','K']
        suits = ['C','D','H','S']
        self.deck = [Card(s,r) for s in suits for r in ranks]
        random.shuffle(self.deck)

    def hand(self, n=1):
        """Deal n cards. Return hand as a Hand object"""
        hand = Hand([self.deck[i] for i in range(n)])
        del self.deck[:n]
        return hand

    def deal(self, cards_per_player, no_of_players):
        """Deal no_of_players hands. Return list of Hand obj"""
        return [self.hand(cards_per_player) for i in range(no_of_players)]

    def putback(self,card):
        """Put back a card under the rest"""
        self.deck.append(card)

    def __str__(self):
        return str(self.deck)

    def __repr__(self):
        return str(self)

    def __len(self):
        return len(self.deck)
