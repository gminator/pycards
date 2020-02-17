from models import *

deck = Deck()
hand = deck.draw()
hand.whats_in_my_hand()
print ("\n\nYour Hand:\n\n%s\n\n" % hand.describe())
