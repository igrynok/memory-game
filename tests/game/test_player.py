import unittest
from game.player import Player
from unittest.mock import patch


class TestPlayer(unittest.TestCase):

    def test_player(self):
        player = Player('Mike')
        self.assertEqual(player.name, 'Mike')
        self.assertEqual(player.score, 0)

    def test_play(self):
        player = Player('John')

        def mock_play(indices, deck):
            return indices[:2]

        with patch.object(Player, 'play', side_effect=mock_play):
            result = player.play([0, 1, 2, 3], 'X X X X')

        self.assertEqual(result, [0, 1])
