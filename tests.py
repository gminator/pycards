import unittest
from models import *

class HandTest(unittest.TestCase):
	def setUp(self):
		self.hearts = Suit(key="\xE2\x99\xA5", name="Hearts")
		self.spades = Suit(key="\xE2\x99\xA0", name="Spades")
		self.clubs = Suit(key="\xE2\x99\xA3", name="Clubs")
		self.diamonds = Suit(key="\xE2\x99\xA6", name="Diamonds")

	def test_cases(self):
		cases = {
			"Scenario: 4 Of A Kind" : ("four_of_kind", True, [self.hearts.cards()[3],self.hearts.cards()[3], self.spades.cards()[3], self.spades.cards()[3]]),
			"Scenario: 4 Of A Kind Failed" : ("four_of_kind", False, [self.hearts.cards()[3],self.hearts.cards()[1], self.spades.cards()[2], self.spades.cards()[1]]),
			"Scenario: Full House" : ("full_house", True, [self.hearts.cards()[3],self.hearts.cards()[3], self.spades.cards()[3],self.hearts.cards()[2], self.spades.cards()[2]]),
			"Scenario: Full House Failed" : ("full_house", False, [self.hearts.cards()[3],self.hearts.cards()[3], self.spades.cards()[3],self.hearts.cards()[2], self.spades.cards()[1]]), 
			"Scenario: Streight" : ("streight", True, [self.hearts.cards()[1],self.hearts.cards()[2], self.spades.cards()[3],self.hearts.cards()[4], self.spades.cards()[5]]), 
			"Scenario: Streight Failed" : ("streight", False, [self.hearts.cards()[1],self.hearts.cards()[1], self.spades.cards()[3],self.hearts.cards()[4], self.spades.cards()[5]]), 
			"Scenario: Streight Flush" : ("streight_flush", True, [self.hearts.cards()[1],self.hearts.cards()[2], self.hearts.cards()[3],self.hearts.cards()[4], self.hearts.cards()[5]]), 
			"Scenario: Streight Flush Failed" : ("streight_flush", False, [self.hearts.cards()[1],self.hearts.cards()[2], self.spades.cards()[3],self.hearts.cards()[4], self.hearts.cards()[5]]), 
			"Scenario: Flush" : ("flush", True, [self.hearts.cards()[4],self.hearts.cards()[2], self.hearts.cards()[3],self.hearts.cards()[6], self.hearts.cards()[5]]), 
			"Scenario: Flush Failed" : ("flush", False, [self.spades.cards()[4],self.hearts.cards()[2], self.hearts.cards()[3],self.hearts.cards()[6], self.hearts.cards()[5]]), 
			"Scenario: 3 Of A Kind" : ("three_pair", True, [self.spades.cards()[4],self.hearts.cards()[4],self.clubs.cards()[4],self.diamonds.cards()[2],self.spades.cards()[5],]), 
			"Scenario: 3 Of A Kind Failed" : ("three_pair", False, [self.spades.cards()[2],self.hearts.cards()[4],self.clubs.cards()[4],self.diamonds.cards()[3],self.spades.cards()[5],]), 
			"Scenario: 1 Pair" : ("two_pair", True, [self.spades.cards()[4],self.hearts.cards()[4],self.clubs.cards()[3],self.diamonds.cards()[2],self.spades.cards()[5],]), 
			"Scenario: 1 Pair Failed" : ("two_pair", False, [self.spades.cards()[2], self.spades.cards()[6]]), 

		}

		for case,params in cases.items(): 
			(method, result, cards) = params
			hand = Hand(cards)  
			operation = getattr(hand, method)  
			print("%s : %s" % (case,hand.describe()))
			self.assertEqual(operation(), result, "%s is not match %s" % (hand.describe(),case))

if __name__ == '__main__':
    unittest.main()