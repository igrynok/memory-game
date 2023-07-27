class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def play(self):
        card1, card2 = input().split()
        return int(card1), int(card2)

    def score_point(self):
        self.score += 1
