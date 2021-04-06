import unittest
from Cards_Deck_Project import Cards, Decks


class CardsTest(unittest.TestCase):
	def setUp(self):
		self.mockCard = Cards('Hearts', 'K')

	def test_init(self):
		self.assertEqual(self.mockCard.suit, 'Hearts')
		self.assertEqual(self.mockCard.value, 'K')

	def test_repr(self):
		self.assertEqual(repr(self.mockCard), 'K of Hearts')
		self.assertEqual(self.mockCard.__repr__(), 'K of Hearts')


class DeckTest(unittest.TestCase):
	def setUp(self):
		self.mockDeck = Decks()

	def test_init(self):
		self.assertIsInstance(self.mockDeck.pack, list)
		self.assertEqual(len(self.mockDeck.pack), 52)

	def test_count(self):
		self.assertEqual(len(self.mockDeck.pack), 52)
		self.mockDeck.pack.pop()
		self.assertEqual(len(self.mockDeck.pack), 51)

	def test_repr(self):
		self.assertEqual(repr(self.mockDeck), 'There are 52 cards in the deck')

	def test_dealFirst(self):
		'''within range'''
		cards = self.mockDeck._dealFirst(15)
		self.assertEqual(len(cards), 15)
		self.assertEqual(len(self.mockDeck.pack), 37)

		self.mockDeck.pack.pop(2)

		'''outside range'''
		cards_ = self.mockDeck._dealFirst(56)
		self.assertEqual(len(cards_), 36)
		self.assertEqual(len(self.mockDeck.pack), 0)

	def test_dealSecond(self):
		'''check equality of the cards'''
		card = self.mockDeck.pack[-1]
		card_deck = self.mockDeck.dealSecond()
		self.assertEqual(card_deck, card)

		'''check overall functionality'''
		self.mockDeck.dealSecond()
		self.assertEqual(len(self.mockDeck.pack), 50)

	def test_dealThird(self):
		'''checks overall functionality'''
		self.mockDeck.dealThird(3)
		self.assertEqual(len(self.mockDeck.pack), 49)

		'''checks correctness of dealing'''
		cards_deal = self.mockDeck.dealThird(31)
		self.assertEqual(len(cards_deal), 31)
		self.assertEqual(self.mockDeck.count(), 18)

	def test_dealThird_Error(self):
		self.mockDeck.dealThird(52)
		with self.assertRaises(ValueError):
			self.mockDeck.dealThird(5)

	def test_shuffle(self):
		'''randomness'''
		prev_deck = self.mockDeck.pack[:]
		# using [:] instead of simple equality
		# as in the latter case 2 variables
		# will point to the same place in memory
		self.mockDeck.shufflePack()
		self.assertNotEqual(self.mockDeck.pack, prev_deck)

		'''len() stays the same'''
		self.mockDeck.shufflePack()
		self.assertTrue(len(self.mockDeck.pack), 52)

	def test_shuffle_full(self):
		'''check that shuffle use only full deck'''
		self.mockDeck.dealSecond()
		with self.assertRaises(ValueError):
			self.mockDeck.shufflePack()


if __name__ == '__main__':
	unittest.main()
