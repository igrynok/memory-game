# memory-game
Design and implementation of the memory game using python.

![image](https://github.com/igrynok/memory-game/assets/2496117/d9571d90-7ba9-4aa7-aee7-d7f94dce5772)

The memory game has following entities:
- **Player** with properties a name and a score.
- **Card** with properties a state (open or not) and a value.
- **Board** with properties a deck size, a queue of players and a list of cards. The board manages the game by keeping track of open and close cards and players in a queue.

**To start the game:**
* Create a Board(n) by specifying the size of the deck. Board will creted a shuffled list of cards with values from 0 to n/2.
* Create players using Player() and add them to the board by calling board.add_player(player)
* Let the game start by calling board.start()
* Each player will be given an opportunity to pick 2 cards in his turn. The player should specify indices of two cards he wants to open. When the player opens two equal cards his score increases.
* The game continues till no closed cards anymore on the board. The player with the highest score wins.  


