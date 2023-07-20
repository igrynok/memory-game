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
        self.players.append(Player)

    def start(self):
        while self.open_cards != self.deck_size:
            player = self.players.popleft()
            pair = player.play(self.get_closed_cards_indices(), self.display())
            while self.cards[pair[0]] == self.cards[pair[1]] and self.open_cards != self.deck_size:
                print(player.name, ' you scored 1 point!')
                self.cards[pair[0]].is_open = True
                self.cards[pair[1]].is_open = True
                self.open_cards += 2
                player.score += 1
                pair = player.play(self.get_closed_cards_indices(), self.display())
            self.players.append(player)

    def get_closed_cards_indices(self) -> List[int]:
        closed_cards = []
        for index, value in enumerate(self.cards):
            if not self.cards[index].is_open:
                closed_cards.append(index)
        return closed_cards

    def get_winner(self):
        pass

    def display(self) -> str:
        out = ''
        for card in self.cards:
            if card.is_open:
                out += str(card.value) + ' '
            else:
                out += 'X '
