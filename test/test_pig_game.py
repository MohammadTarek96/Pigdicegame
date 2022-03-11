

import unittest
from pig.core.game import Game, Dice
from pig.core.player import BotPlayer, Player, LowRiskStrategy
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

    def test_end_turn(self):
        player = Player("player")
        second_player = Player("second")
        game = Game()
        game.dice = Dice([6])
        game.players = [player, second_player]
        
        # without any rolls score should be 0, turn moves to next
        game.end_turn_for_current_player()
        # assert no changes in score, but a change in turn
        self.assertEqual(0, player.score)
        self.assertEqual(0, player.current_turn_score)
        self.assertEqual(1, game.turn)

        # rolled two 6s for the second player
        game.roll_for_current_player()
        game.roll_for_current_player()
        game.end_turn_for_current_player()
        # assert that the turn ended: next turn, and the player has 12 point added to his score
        self.assertEqual(12, second_player.score)
        # assert that his current_turn_score has ended
        self.assertEqual(0, second_player.current_turn_score)
        self.assertEqual(0, game.turn)

    def test_check_if_game_ended_no_players(self):
        player = Player("p1")
        player_2 = Player("p2")
        game = Game()
        game.players = [player,player_2]
        # check for the game state, and method return value
        self.assertFalse(game.check_if_game_ended())
        self.assertFalse(game.game_ended)

    def test_check_if_game_ended_one_player(self):
        player = Player("p1")
        player.score = 103

        player_2 = Player("p2")
        player_2.score = 95
        game = Game()
        game.dice = Dice([6,6,1,6,1])
        game.players = [player, player_2]
        self.assertTrue(game.check_if_game_ended())
        self.assertTrue(game.game_ended)
        # assert that the game did not do a end of game simulation
        self.assertEqual(103, player.score)
        self.assertEqual(95, player_2.score)

    def test_check_if_game_ended_multiple_players(self):
        player = Player("p1")
        player.score = 105

        player_2 = Player("p2")
        player_2.score = 103

        player_3 = Player("p3")
        player_3.score = 10

        game = Game()
        game.dice = Dice([6, 6, 1, 6, 1])
        game.players = [player, player_2, player_3]

        self.assertTrue(game.check_if_game_ended())
        self.assertTrue(game.game_ended)
        
        # check that it did simulate rolls
        self.assertEqual(105 + 6 + 6, player.score)
        self.assertEqual(103 + 6, player_2.score)
        self.assertEqual(10, player_3.score)

    def test_cheat(self):
        player = Player("p1")
        game = Game()
        game.players = [player]
        # cheat, current score = 90
        game.cheat_for_current_player(90)
        self.assertEqual(90, player.current_turn_score)
        # Make sure that the cheat only happens once
        game.roll_for_current_player()
        self.assertNotEqual(180, player.current_turn_score)

    def test_for_bot(self):
        bot_player = BotPlayer("bot", LowRiskStrategy())
        player = Player("")

        game = Game()
        game.players = [bot_player, player]
        game.dice = Dice([4, 2, 3, 1])

        game.play_for_bot()
        
        self.assertEqual(9, bot_player.score)
        self.assertEqual(0, player.current_turn_score)
        self.assertEqual(1, game.turn)

    def test_multiple_bots(self):
        bot_player = BotPlayer("bot", LowRiskStrategy())
        bot_player_2 = BotPlayer("bot-2", LowRiskStrategy())
        player = Player("")
        game = Game()
        game.players = [bot_player, bot_player_2, Player(" ")]
        game.dice = Dice([6, 1, 2, 3, 6, 1])
        
        game.play_for_bot()
        
        self.assertEqual(0, bot_player.score)
        self.assertEqual(2 + 3 + 6, bot_player_2.score)
        self.assertEqual(2, game.turn)
