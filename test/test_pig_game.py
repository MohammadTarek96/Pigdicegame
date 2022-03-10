

import unittest
from pig.core.game import Game
from pig.core.exceptions import TooManyPlayersError


class GameTest(unittest.TestCase):

    def test_adding_new_player():
        
        game = Game()
        # check that the game's player list is empty at the beggining
        self.assertEqual(game.get_player_count(), 0) 

        # adding one player increases the player by 1
        game.add_new_cpu_player()
        self.assertEqual(game.get_player_count(), 1)


    def test_adding_new_player_beyond_limit():

        game = Game()
        
        # adding more then 4 players will throw an error
        with self.assertRaises(TooManyPlayersError):
            for i in range(5):
                game.add_new_cpu_player()

