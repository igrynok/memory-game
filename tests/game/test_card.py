import unittest
from game.model.card import Card


class TestCard(unittest.TestCase):

    def test_card(self):
        card = Card(10)
        self.assertEqual(card.value, 10)
        self.assertEqual(card.is_open, False)
