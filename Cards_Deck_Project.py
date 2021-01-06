from random import shuffle
class Cards:

	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Decks:

	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		self.pack = [Cards(x,y) for x in suits for y in values]

	def count(self):
		return len(self.pack)

	def __repr__(self):
		return f"There are {self.count()} cards in the deck"

	# _ will mean that this method is for internal use only
	def _dealFirst(self,num):
		curr = self.count()
		maxy = min(curr,num)
		try:
			to_del = self.pack[-maxy:]
			self.pack = self.pack[:-maxy]
		except ValueError:
			return "No more cards in the pack"
		return to_del

	def shufflePack(self):
		if self.count() < 52:
			raise ValueError('Only full packs can be shuffled')
		shuffle(self.pack)
		return self

	#this method will return only one card from the pack dealt
	def dealSecond(self):
		to_return = self._dealFirst(1)
		print(f"This time {to_return[0]} will be removed")
		return to_return[0]

	#deal the particular number of cards
	def dealThird(self,num):
		removed = self._dealFirst(num)
		print(f"There will be {removed} dealt")
		return removed

deck1 = Decks()
deck1.shufflePack()

#below line will prove that shuffling was successful
print(deck1.pack)

deck1.dealSecond()

