
from random import choice

class Player:
    score = 0
    current_turn_score = 0

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"<{self.name}, score: {self.score}>"

    def finish_turn(self):
        self.score += self.current_turn_score
        self.current_turn_score = 0

class HumanPlayer(Player):
    pass


class BotPlayer(Player):
    strategy = None
    def __init__(self, name, strategy = None):
        super().__init__(name)
        if strategy is None:
            strategy = choice([LowRiskStrategy(), MediumRiskStrategy(), HighRiskStrategy()])

        self.strategy = strategy


class Strategy:
    threshold = 0

    def should_roll(self, current_score):
        return current_score <= self.threshold

class LowRiskStrategy(Strategy):
    threshold = 6

class MediumRiskStrategy(Strategy):
    threshold = 12

class HighRiskStrategy(Strategy):
    threshold = 18
