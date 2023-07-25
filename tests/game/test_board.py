import unittest
import random

from game.board import Board
from game.player import Player
from unittest.mock import patch


class TestBoard(unittest.TestCase):

    def test_board(self):
        board = Board(10)
        self.assertEqual(board.deck_size, 10)
        self.assertEqual(len(board.cards), 10)
        # check the count of 0 in the deck
        card_values = [c.value for c in board.cards]
        self.assertEqual(card_values.count(0), 2)
        # check that all cards are closed
        closed_cards = [c for c in board.cards if not c.is_open]
        self.assertEqual(len(closed_cards), 10)
        # check the number of players
        self.assertEqual(len(board.players), 0)

    def test_add_player(self):
        board = Board(10)
        self.assertEqual(len(board.players), 0)
        board.add_player(Player('Tom'))
        board.add_player(Player('Mike'))
        self.assertEqual(len(board.players), 2)

    def test_start_game(self):
        board = Board(4)
        board.add_player(Player('Tim'))
        board.add_player(Player('Elsa'))

        def mock_play(indices, deck):
            return random.sample(indices, 2)

        with patch.object(Player, 'play', side_effect=mock_play):
            board.start_game()

        self.assertEqual(board.open_cards, 4)