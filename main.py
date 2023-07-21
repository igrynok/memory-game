from game.board import Board
from game.player import Player

if __name__ == '__main__':
    print('Creating a board with 6 cards')
    board = Board(6)
    p1 = Player('Andy')
    p2 = Player('Mike')
    print('Adding players Andy and Mike')
    board.add_player(p1)
    board.add_player(p2)
    print('Starting the game...')
    board.start()
    print('')
    print('Leaderboard:')
    for p in board.players:
        print(f"{p.name}'s score: {p.score}")
