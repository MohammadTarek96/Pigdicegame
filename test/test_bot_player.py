
import unittest
from pig.core.player import BotPlayer, Strategy

class TestBotPlayer(unittest.TestCase):

    def test_initialization(self):
        bot = BotPlayer("bot")
        self.assertIsInstance(bot.strategy, Strategy)
