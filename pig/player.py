"""Module containing all the player classes and the bot strategies."""
from random import choice


class Player:
    """A class that holds the information about the player."""

    score = 0
    current_turn_score = 0

    def __init__(self, name):
        """Configure the instance with it's name."""
        self.name = name

    def change_name(self, new_name):
        """Change the name to the value of new_name."""
        self.name = new_name

    def __str__(self):
        """Return a string representing the object."""
        return f"<{self.name}, score: {self.score}>"

    def finish_turn(self):
        """Finishe a player's turn."""
        self.score += self.current_turn_score
        self.current_turn_score = 0


class HumanPlayer(Player):
    """Separate class to identify human players."""

    pass


class BotPlayer(Player):
    """A bot player. Has a strategy that dictates it's decisions."""

    strategy = None

    def __init__(self, name, strategy=None):
        """Configure the bot, with a name and strategy."""
        super().__init__(name)
        # if no strategy is provided, one is chosen at random
        if strategy is None:
            strategy = choice(
                [LowRiskStrategy(), MediumRiskStrategy(), HighRiskStrategy()]
            )
        self.strategy = strategy


class Strategy:
    """Class used to take decisions for the bots."""

    threshold = 0

    def should_roll(self, current_score):
        """Return true if the decision is to play, false otherwise."""
        return current_score <= self.threshold


class LowRiskStrategy(Strategy):
    """LowRiskStrategy for a bot, with the threshold of 6."""

    threshold = 6


class MediumRiskStrategy(Strategy):
    """MediumRiskStrategy for a bot, with the threshold of 12."""

    threshold = 12


class HighRiskStrategy(Strategy):
    """HighRiskStrategy for a bot, with the threshold of 18."""

    threshold = 18
