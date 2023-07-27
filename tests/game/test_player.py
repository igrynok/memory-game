import unittest
from game.model.player import Player
from unittest.mock import patch


class TestPlayer(unittest.TestCase):

    def test_player(self):
        player = Player('Mike')
        self.assertEqual(player.name, 'Mike')
        self.assertEqual(player.score, 0)
