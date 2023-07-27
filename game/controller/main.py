from game.model.board import Board
from game.model.player import Player
from game.view.board_view import BoardView
from game.view.player_view import PlayerView

if __name__ == '__main__':

    print('Creating a board with 6 cards')
    board = Board(6)
    p1 = Player('Andy')
    p2 = Player('Mike')
    print('Adding players Andy and Mike')
    board.add_player(p1)
    board.add_player(p2)
    print('Starting the game...')

    player = board.get_next_player()
    while len(board.get_closed_cards_indices()) > 0:
        print('')
        print(player.name, ' your turn. Pick two cards from the deck (indices):')
        print(BoardView.view(board))
        print(str(board.get_closed_cards_indices()))
        card1_id, card2_id = player.play()
        board.open_cards_from_deck(card1_id, card2_id)
        print(BoardView.view(board))
        if board.check_cards_equal(card1_id, card2_id):
            print(player.name, 'you scored 1 point!')
            player.score_point()
        else:
            board.close_cards_from_deck(card1_id, card2_id)
            print(player.name, 'better luck next time!')
            board.add_player_to_queue(player)
            player = board.get_next_player()
    board.add_player_to_queue(player)

    print('')
    print('Leaderboard:')
    for p in board.players:
        print(PlayerView.view(p))
    winner = board.get_winner()

    print('')
    print('The winner is:')
    print(PlayerView.view(winner))

