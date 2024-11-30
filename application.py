from checker import Checker
from deck import Deck
from hand import Hand
from stats import Stats


class Application:
    def __init__(self):
        self.stats = Stats()
        self.stats.load_stats()

    def run(self):
        while True:
            deck = Deck()
            hand = Hand()

            for _ in range(5):
                hand.add_card(deck.deal_card())

            print("Your hand:")
            hand.show_hand()

            replace_indices = input("Enter the card numbers to replace (separated by spaces), or press Enter to keep all cards: ").strip()
            if replace_indices:
                replace_indices = list(map(int, replace_indices.split()))
                for index in replace_indices:
                    hand.replace_card(index - 1, deck.deal_card())

            print("Your final hand:")
            hand.show_hand()

            checker = Checker(hand)
            result, points = checker.check_hand()
            print(f"Result: {result} ({points} points)")

            self.stats.increment_combination(result)

            command = input("Enter 'stats' to see statistics, 'play' to play again, or 'exit' to quit: ").strip().lower()
            if command == 'stats':
                self.stats.show_stats()
            elif command == 'exit':
                break

        self.stats.save_stats()
