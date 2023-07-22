import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):

    def test_player(self):
        player = Player('Mike')
        self.assertEqual(player.name, 'Mike')
        self.assertEqual(player.score, 0)