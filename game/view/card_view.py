class CardView:

    @staticmethod
    def view(card):
        return str(card.value) if card.is_open else 'X'
