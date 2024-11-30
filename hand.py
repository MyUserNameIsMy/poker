class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if len(self.cards) >= 5:
            raise ValueError("Hand cannot have more than 5 cards")
        self.cards.append(card)

    def replace_card(self, index, new_card):
        if index < 0 or index >= len(self.cards):
            raise IndexError("Invalid card index")
        self.cards[index] = new_card

    def show_hand(self):
        print('  |  '.join(str(i) for i in range(1, 6)))
        print(' |  '.join(str(card) for card in self.cards))

    def __str__(self):
        return ' | '.join(str(card) for card in self.cards)
