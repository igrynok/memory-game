# memory-game
Design and implementation of the memory game using python.

![image](https://github.com/igrynok/memory-game/assets/2496117/53883e68-c929-43b1-bfca-d5bad1a8972b)

The memory game has following entities:
# **Player** with properties a name and a score.
# **Card** with properties a state (open or not) and a value.
# **Board** with properties a deck size, a queue of players and a list of cards. The board manages the game by keeping track of open and close cards and players in a queue.

**To start the game:**
* Create a Board(n) by specifizing the size of the deck. Board will creted a shuffled list of cards with values from 1 to n/2.
* Create players Player() and add them the board board.add_player(player)
* Let the game start by claling board.start()
* Each player will be given an opportunity to pick 2 cards in his turn. The player should specify indices of two cards he wants to open. When the player opens two equal cards his score increases.
* The game continues till no closed cards anymore on the board. The player with the highest score wins.  


