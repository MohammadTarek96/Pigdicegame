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
    game_ended = False

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

    def round_end(self):
        self.check_if_game_ended()
        print(self.leaderboard())

    def leaderboard(self):
        return "Leaderboard:\n" + "\n".join(map(lambda x: f"{x[0]+1}) {x[1].name}: {x[1].score}",
            enumerate(sorted(self.players,key=lambda x: x.score, reverse=True))))

    def check_if_game_ended(self):
        """
        The function checks whether the game has ended, and simulates a roll sequence for everyone over 100
        :return: bool, True if the game has ended, k
        """
        players_over_100 = list(filter(lambda x: x.score > 100, self.players))
        # No winners
        if len(players_over_100) == 0: 
            return False
        
        if len(players_over_100) == 1:
            self.game_ended = True
            print(f"AAAAAAAAAAAAnd the winner iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiis: {players_over_100[0].score}")
            return True

        print("Multiple winners! Rolling for everyone until they hit a 1")
        for i in players_over_100:
            while True:
                print(f"Rolling for {i.name}")
                roll = self.dice.roll()
                if roll == 1:
                    print(f"Rolled a 1. Final score for {i.name} is {i.score}")
                    break
                i.score += roll
                print(f"Rolled a {roll}. {i.name}'s score is {i.score}")
        
        winner = sorted(players_over_100, key=lambda x: x.score, reverse=True)[0]
        self.game_ended = True
        print(f"The results are in. The winner is {winner.name}, with a score of {winner.score}")
        return True

    def cheat_for_current_player(self, score):
        # A little magic trick 
        old_dice = self.dice
        self.dice = Dice([score])
        self.roll_for_current_player()
        self.dice = old_dice
        if score < 0 or score > 6:
            print(f"Huh? That is weird and unbelievable!!! The {self.players[self.turn].name} just rolled for {score}")

            

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
