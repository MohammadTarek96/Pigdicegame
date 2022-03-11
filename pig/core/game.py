#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .player import Player, BotPlayer
from .exceptions import TooManyPlayersError
from random import randint

class Game: 
    """
    The class that will hold the data about the player,
    and will invoke the methods of the non-human players.
    """

    players = None
    turn = 0

    def __init__(self):
        """ Start the game and the number of the players"""
        self.players = []
        self.dice = Dice()


    def get_player_count(self):
        """ 
        :return: int - the list of players that are currently in the game
        """
        return len(self.players)


    def add_new_player(self, new_player = None):
        """
        Adds a new player to the game, if there is a free spot. The game is limited to 4 players.
        :param new_player: the new player that will be added. if the new player is not provided, a bot player will be added
        :return : the instance of the new player
        """
        
        # check the length of the list
        if (self.get_player_count() == 4): 
            raise TooManyPlayersError()

        if new_player is None:
            new_player = BotPlayer(f"bot - {randint(1000,9999)}")
        self.players.append(new_player)

        return new_player

    def roll_for_current_player(self):
        """
        Performs a roll for the current player.
        :return : bool - true if it ends the turn, false otherwise
        """
        roll = self.dice.roll()
        current_player = self.players[self.turn]
        # lose condition
        if (roll == 1):
            print(f"\t{current_player.name} rolled a {roll}")
            current_player.current_turn_score = 0
            self.end_turn_for_current_player()
            return True
        
        current_player.current_turn_score += roll
        print(f"\t{current_player.name} rolled a {roll}. His current turn score is {current_player.current_turn_score}")

        return False

    def end_turn_for_current_player(self):
        roll = self.dice.roll()
        current_player = self.players[self.turn]
        current_player.finish_turn()
        print(f"\tTurn ends. Total accumulated score {current_player.score}")
        # move to the next turn, circling back to 0 if it reached the end
        self.turn = (self.turn + 1) % self.get_player_count()

        if isinstance(self.players[self.turn], BotPlayer):
            self.end_turn_for_current_player()

        if self.turn == 0:
            self.round_end()
            self.check_for_game_end()

    def do_leaderboard(self):
        print(self.leaderboard())

    def round_end(self):
        print(self.leaderboard())

    def leaderboard(self):
        return "Leaderboard:\n" + "\n".join(map(lambda x: f"{x[0]+1}) {x[1].name}: {x[1].score}",
            enumerate(sorted(list(self.players),key=lambda x: x.score, reverse=True))))

    def check_for_game_end(self):
        pass

class Dice:
    """
    Class that will be responsible for the random parts of the game. Provides a test configuration, that will return 
    the numbers provided in the list
    """
    test_list = None
    test_index = 0
    def __init__(self, test_list = None):
        self.test_list = test_list

    
    def roll(self):
        if (self.test_list is None):
            return randint(1,6)
        x = self.test_list[self.test_index]
        self.test_index = (self.test_index + 1) % len(self.test_list)
        return x
