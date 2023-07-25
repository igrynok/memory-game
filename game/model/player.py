from typing import List


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def play(self, indices, deck):
        print('')
        print(self.name, ' your turn. Pick two cards from the deck:')
        print(deck)
        print('Available indices:', str(indices))
        card1, card2 = input().split()
        return int(card1), int(card2)
