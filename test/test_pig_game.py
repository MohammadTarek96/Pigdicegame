

import unittest
from pig.core.game import Game, Dice
from pig.core.player import BotPlayer, Player
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

   
    def test_leaderboard(self):
        expected = """Leaderboard:
1) player: 60
2) bot-1: 30"""
        game = Game()
        p1 = Player("player")
        p1.score = 60

        p2 = Player("bot-1")
        p2.score = 30

        game.players = [p2, p1]
        self.assertEqual(expected, game.leaderboard())

    def test_roll_for_current_player(self):
        player = Player("player")

        game = Game()
        game.dice = Dice([6,1])
        game.players = [player, Player('_')]

        # assert that the turn has not ended
        self.assertFalse(game.roll_for_current_player())
        # check the the roll is counted, but not to the total score
        self.assertEqual(6, player.current_turn_score)
        self.assertEqual(0, player.score)

        # assert that the turn has ended, returned true
        self.assertTrue(game.roll_for_current_player())
        # a 1 has been rolled, ended turn
        self.assertEqual(0, player.current_turn_score)
        self.assertEqual(0, player.score)
        self.assertEqual(1, game.turn)


