from card import Card


class Checker:
    def __init__(self, hand):
        self.hand = hand

    def check_hand(self):
        ranks = sorted([card.rank for card in self.hand.cards], key=lambda x: Card.RANKS.index(x))
        suits = [card.suit for card in self.hand.cards]

        if self.is_royal_flush(ranks, suits):
            return "Royal Flush", 10
        elif self.is_straight_flush(ranks, suits):
            return "Straight Flush", 9
        elif self.is_four_of_a_kind(ranks):
            return "Four of a Kind", 8
        elif self.is_full_house(ranks):
            return "Full House", 7
        elif self.is_flush(suits):
            return "Flush", 6
        elif self.is_straight(ranks):
            return "Straight", 5
        elif self.is_three_of_a_kind(ranks):
            return "Three of a Kind", 4
        elif self.is_two_pairs(ranks):
            return "Two Pairs", 3
        elif self.is_pair(ranks):
            return "Pair", 2
        else:
            return "High Card", 1

    def is_royal_flush(self, ranks, suits):
        return ranks == ["10", "J", "Q", "K", "A"] and len(set(suits)) == 1

    def is_straight_flush(self, ranks, suits):
        return self.is_straight(ranks) and len(set(suits)) == 1

    def is_four_of_a_kind(self, ranks):
        return any(ranks.count(rank) == 4 for rank in ranks)

    def is_full_house(self, ranks):
        rank_counts = {rank: ranks.count(rank) for rank in ranks}
        values = list(rank_counts.values())
        return 3 in values and 2 in values

    def is_flush(self, suits):
        return len(set(suits)) == 1

    def is_straight(self, ranks):
        rank_indices = [Card.RANKS.index(rank) for rank in ranks]
        return all(rank_indices[i] + 1 == rank_indices[i + 1] for i in range(4))

    def is_three_of_a_kind(self, ranks):
        return any(ranks.count(rank) == 3 for rank in ranks)

    def is_two_pairs(self, ranks):
        rank_counts = {rank: ranks.count(rank) for rank in ranks}
        values = list(rank_counts.values())
        return values.count(2) == 2

    def is_pair(self, ranks):
        return any(ranks.count(rank) == 2 for rank in ranks)
