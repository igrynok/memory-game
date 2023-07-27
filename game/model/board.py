from typing import List

from game.model.card import Card
from game.model.player import Player
from collections import deque
import random


class Board:

    def __init__(self, deck_size=10):
        self.deck_size = deck_size
        self.players = deque()
        cards = []
        for i in range(int(self.deck_size/2)):
            cards.append(Card(i))
            cards.append(Card(i))
        random.shuffle(cards)
        self.cards = cards
        self.open_cards = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def get_next_player(self):
        return self.players.popleft()

    def get_closed_cards_indices(self) -> List[int]:
        closed_cards = []
        for index, value in enumerate(self.cards):
            if not self.cards[index].is_open:
                closed_cards.append(index)
        return closed_cards

    def get_winner(self):
        scores = [player.score for player in self.players]
        index = scores.index(max(scores))
        return self.players[index]

    def open_cards_from_deck(self, card1_id, card2_id):
        self.cards[card1_id].is_open = True
        self.cards[card2_id].is_open = True
        self.open_cards += 2

    def close_cards_from_deck(self, card1_id, card2_id):
        self.cards[card1_id].is_open = False
        self.cards[card2_id].is_open = False
        self.open_cards -= 2

    def check_cards_equal(self, card1_id, card2_id):
        return self.cards[card1_id].value == self.cards[card2_id].value

    def add_player_to_queue(self, player):
        self.players.append(player)
