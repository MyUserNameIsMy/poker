import json

class Stats:
    COMBINATIONS = [
        "Royal Flush", "Straight Flush", "Four of a Kind", "Full House",
        "Flush", "Straight", "Three of a Kind", "Two Pairs", "Pair", "High Card"
    ]

    def __init__(self):
        self.stats = {combination: 0 for combination in self.COMBINATIONS}

    def load_stats(self, filename='stats.json'):
        try:
            with open(filename, 'r') as file:
                self.stats = json.load(file)
        except FileNotFoundError:
            self.stats = {combination: 0 for combination in self.COMBINATIONS}

    def save_stats(self, filename='stats.json'):
        with open(filename, 'w') as file:
            json.dump(self.stats, file)

    def increment_combination(self, combination):
        if combination in self.stats:
            self.stats[combination] += 1
        else:
            raise ValueError(f"Invalid combination: {combination}")

    def show_stats(self):
        print("Statistics:")
        for combination in self.COMBINATIONS:
            print(f"{combination}: {self.stats[combination]}")
