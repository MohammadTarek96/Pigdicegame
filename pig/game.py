#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module that hold the information about the Game class."""

from random import randint

from exceptions import TooManyPlayersError
from player import BotPlayer, HumanPlayer


class Game:
    """Class representing the game.

    Holds the information about the players, the dice and if needed invokes
    the bot actions.
    """

    players = None
    turn = 0
    rounds = 1
    game_ended = False

    def __init__(self):
        """Start the game and the number of the players."""
        self.players = []
        self.dice = Dice()

    def get_player_count(self):
        """Getter for the player count.

        :return: int - the list of players that are currently in the game
        """
        return len(self.players)

    def add_new_player(self, new_player=None):
        """
        Add a new player to the game, if there is a free spot.

        The game is limited to 4 players.
        :param new_player: the new player that will be added. if the
         new player is not provided, a bot player will be added
        :return : the instance of the new player
        """
        # check the length of the list
        if self.get_player_count() == 4:
            raise TooManyPlayersError()

        if new_player is None:
            new_player = BotPlayer(f"bot - {randint(1000, 9999)}")
        self.players.append(new_player)

        return new_player

    def roll_for_current_player(self):
        """
        Perform a roll for the current player.

        :return : bool - true if it ends the turn, false otherwise
        """
        roll = self.dice.roll()
        current_player = self.players[self.turn]
        # lose condition
        if roll == 1:
            print(f"\t{current_player.name} rolled a {roll}")
            current_player.current_turn_score = 0
            self.end_turn_for_current_player()
            return True

        current_player.current_turn_score += roll
        print(f"\t{current_player.name} rolled a {roll}. His current"
              f"turn score is {current_player.current_turn_score}")

        return False

    def end_turn_for_current_player(self):
        """Operations to be done at the end of turn."""
        # display a report with the player's accumulated score
        current_player = self.players[self.turn]
        current_player.finish_turn()
        print(f"\tTurn ends. Total accumulated score {current_player.score}")

        # move to the next turn, circling back to 0 if it reached the end
        self.turn = (self.turn + 1) % self.get_player_count()
        # since self.turn will be changed by bot play, keep a copy
        turn = self.turn

        # play for bots until the next player is a human
        while isinstance(self.players[self.turn], BotPlayer):
            self.play_for_bot()

        # when the turn goes back to 0, it's a round end
        if turn == 0:
            self.round_end()

        # let the player know whose turn it is
        current_player = self.players[turn]
        if isinstance(current_player, HumanPlayer):
            print(f"it's {current_player.name}'s turn!")

    def play_for_bot(self):
        """Play for the bot, by using his defined strategy."""
        current_player = self.players[self.turn]
        while True:
            # roll, if the bot strategy says so
            if current_player.strategy.should_roll(
                    current_player.current_turn_score):
                # check if the roll ended the bot's turn (rolled a 1)
                if self.roll_for_current_player():
                    break
            else:
                # if the bot decided to quit, end the turn
                self.end_turn_for_current_player()
                break

    def round_end(self):
        """Finishes a round, doing all the end-of-round operations."""
        self.rounds += 1
        self.check_if_game_ended()
        print(self.leaderboard())

    def leaderboard(self):
        """Return a leaderboard, sorted by score."""
        return "Leaderboard:\n" + "\n".join(
            map(lambda x: f"{x[0] + 1}) {x[1].name}: {x[1].score}",
                enumerate(sorted(self.players, key=lambda x: x.score,
                                  reverse=True))))

    def check_if_game_ended(self):
        """Check whether the game has ended.

        Check if the game has any winner, by counting the number of
        players over 100 points, and if there are multiple, it declares
        a draw
        :return: bool, True if the game has ended, False otherwise
        """
        players_over_100 = list(filter(lambda x: x.score >= 100, self.players))
        # No winners
        if len(players_over_100) == 0:
            return False

        # only one win
        if len(players_over_100) == 1:
            self.game_ended = True
            print(f"AAAAAAAAAAAAnd the winner iiiiiiiiiiiiiiiiiiiiiii"
                  f"iiiiiiiiiiis: {players_over_100[0].name}")
            print(f"Took {self.rounds} rounds to complete the game!")
            return True

        print("Multiple winners! Draw!")
        print(f"Took {self.rounds} rounds to complete the game!")
        self.game_ended = True
        return True

    def cheat_for_current_player(self, score):
        """Cheat for the current player.

        Add the score defined in the method to the current_score
        Score = 1 will be treated as normal
        :param score: the score that the player gets
        """
        # A little magic trick, create and pass a cheat-dice
        # for one roll, and then go back to the default one
        old_dice = self.dice
        self.dice = Dice([score])
        self.roll_for_current_player()
        self.dice = old_dice

        # display a message for the player
        if score < 0 or score > 6:
            print(f"Huh? That is weird and unbelievable!!! The"
                  f"{self.players[self.turn].name} just rolled for {score}")


class Dice:
    """Class that holds the information about the dice.

    Is responsible for the random parts of the game.
    Provides a test configuration, that will return the numbers provided
    in the list
    """

    test_list = None
    test_index = 0

    def __init__(self, test_list=None):
        """Initialize the test_list with the value provided.

        :param test_list: list[int] - the list that the dice should return
        """
        self.test_list = test_list

    def roll(self):
        """Perform a roll.

        When test_list is not defined (default behavior)
            Return a random number between 1 and 6
        When test_list is defined:
            Return the value at test_index and increases it
        """
        if self.test_list is None:
            return randint(1, 6)
        x = self.test_list[self.test_index]
        self.test_index = (self.test_index + 1) % len(self.test_list)
        return x
