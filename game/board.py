from typing import List

from game.card import Card
from game.player import Player
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

    def start(self):
        while self.open_cards != self.deck_size:
            player = self.players.popleft()
            card1_id, card2_id = player.play(self.get_closed_cards_indices(), self.display())
            print(self.display(card1_id, card2_id))
            while self.cards[card1_id].value == self.cards[card2_id].value and self.open_cards != self.deck_size:
                print(player.name, ' you scored 1 point!')
                self.cards[card1_id].is_open = True
                self.cards[card2_id].is_open = True
                self.open_cards += 2
                player.score += 1
                if self.open_cards != self.deck_size:
                    card1_id, card2_id = player.play(self.get_closed_cards_indices(), self.display())
                print(self.display(card1_id, card2_id))
            self.players.append(player)

    def get_closed_cards_indices(self) -> List[int]:
        closed_cards = []
        for index, value in enumerate(self.cards):
            if not self.cards[index].is_open:
                closed_cards.append(index)
        return closed_cards

    def get_winner(self):
        pass

    def display(self, card1_id=None, card2_id=None) -> str:
        out = ''
        for card_id, card in enumerate(self.cards):
            if card.is_open or card_id == card1_id or card_id == card2_id:
                out += str(card.value) + ' '
            else:
                out += 'X '
        return out
