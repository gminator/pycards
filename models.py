import random

class Suit(object):
	"""
	Suit Model 
	
	This mode used to establish the suits need for the create of a deck
	"""
	options = (("\xE2\x99\xA5", "Hearts"), ("\xE2\x99\xA0", "Spades"), ("\xE2\x99\xA3", "Clubs"), ("\xE2\x99\xA6","Diamonds"))

	name =None
	key = None

	def __init__(self, **kwargs): 
		self.name 	= kwargs["name"]
		self.key 	= kwargs["key"]
	
	@staticmethod
	def deck():
		"""
		Suits

		Create one full Deck
		Contain 4 Suits 
		"""
		suits = []
		for i in Suit.options: 
			(key,name) = i 
			suits.append(Suit(key=key,name=name)) 

		return suits

	def shuffle(self,): 
		cards = self.cards()
		random.shuffle(cards) 
		return cards

	def cards(self,):
		cards = []
		for i in Card.cards:
			cards.append(Card(i, self, len(cards)))
		return cards
		

	def __str__(self,):
		return "%s - %s" % (self.name, len(self.cards()))


class Card(object):

	suit = None
	key = None
	number = None

	cards = list(range(1,10)) + ["J", "Q", "K", "A"]

	def __init__(self,card,suit,index):
		self.number = card
		self.suit = suit
		self.key = index

	def __str__(self,):
		return "%s%s" % (self.number,self.suit.key)



class Deck(object):
	#Standard Poker Deck Size
	decks = 1
	deck = None

	def __init__(self,):
		self.deck =[]
		for i in range(0, Deck.decks):
			self.deck.append(Suit.deck())

	

	def shuffle(self,):
		cards = []

		for decks in self.deck: 
			for suit in decks:  
				cards += suit.shuffle()
		random.shuffle(cards)
		return cards

	def draw(self,):
		cards = self.shuffle()
		hand = cards[0:5] 
		return Hand(hand)

class Hand(object):

	def __init__(self,cards):
		self.cards = cards
		

	def describe(self,):
		cards = []
		for card in self.cards:
			cards.append(str(card)) 
		return " ".join(cards)

	def whats_in_my_hand(self):
		pass
		#self.kinds()

	def kinds(self,total):
		kinds = {}
		hands = []
		for card in self.cards: 
			if card.number not in kinds: kinds[card.number] = []
			kinds[card.number].append(card)
		
		for n,cards in kinds.items():
			if len(cards) == total: 
				return Hand(cards)
				

		return False

	def full_house(self,):
		return self.two_pair() and self.three_pair()

	def two_pair(self,):
		kinds = self.kinds(2)
		if kinds:
			return True
		return False
	
	def three_pair(self,):
		kinds = self.kinds(3)
		if kinds:return True
		return False

	def four_of_kind(self,):
		kinds = self.kinds(4)
		if kinds:return True
		return False

	def flush(self,):
		l = [card.suit.key for card in self.cards] 
		return len(set(l)) == 1

	def streight_flush(self,): 
	 	return self.streight() and self.flush()

	def streight(self,):
		l = [card.key for card in self.cards]  
		return sorted(l) == list(range(min(l), max(l)+1)) 

