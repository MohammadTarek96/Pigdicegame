import unittest
from pig.player import HumanPlayer


class TestHumanPlayer(unittest.TestCase):
    def test_initialization(self):

        name = "john dice"
        player = HumanPlayer(name)

        self.assertIsInstance(player, HumanPlayer)
        self.assertEqual(name, player.name)

    def test_change_name(self):
        name = "john dice"
        player = HumanPlayer(name)

        new_name = "james dice"
        player.change_name(new_name)

        self.assertEqual(new_name, player.name)
