# Cards-Deck-project
It's a small project that uses Python **OOP** simple methods and techniques. 

There are two classes: `Cards` and `Decks` where every card is a separate `Card` class that 
finds itself in a list of similar cards in `Decks` class.

`Decks` class comprises a couple of methods done over pack of Cards.

1. `count()` current number of cards in the pack
2. `shuffle()` the pack to randomize cards
3. `deal()` one card from the pack
4. `deal()` multiple cards from the pack
 + those 2 aforewritten methods use another method to see whether it's possible
   to remove cards (i.e. current number of them > 0) and also take the smallest
   value between user input number and current number of cards in the pack.

<br>
<h4>Tests</h4>

Also, I've written Unit tests for this project to check the functionality. 
They will mimick the created Card/Deck and check all the aforewritten methods
from various angles.

Note: when checking randomness `[:]` is used instead of simple `copy()` or `=`
      as `[:]` variables won't point at the same place in memory whilst latter
      ones will.
