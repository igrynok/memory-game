from typing import List


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def play(self, indices: List[int], deck) -> tuple:
        print(self.name, ' your turn. Pick two cards from the deck:')
        print(deck)
        print('Available indices:', ' '.join(str(indices)))
        card1, card2 = input().split()
        return int(card1), int(card2)
