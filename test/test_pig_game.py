

import unittest
from pig.core.game import Game
from pig.core.player import BotPlayer
from pig.core.exceptions import TooManyPlayersError


class TestGame(unittest.TestCase):
    """ Tests the game class """

    def test_adding_new_player(self):
        """ Tests the functionality of adding a new player to the list of players, by checking the list length and the return type """
        game = Game()
        # check that the game's player list is empty at the beggining
        self.assertEqual(0, game.get_player_count()) 

        # adding one player increases the player by 1
        new_player = game.add_new_player()
        self.assertEqual(1, game.get_player_count())

        # ensure that the new instance is of a player
        self.assertIsInstance(new_player, BotPlayer)


    def test_adding_new_player_beyond_limit(self):

        game = Game()
        
        # adding more then 4 players will throw an error
        with self.assertRaises(TooManyPlayersError):
            for _ in range(6):
                game.add_new_player()

