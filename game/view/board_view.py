from game.view.card_view import CardView


class BoardView:

    @staticmethod
    def view(board):
        return ' '.join([CardView.view(card) for card in board.cards])
