#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .player import Player

class Game: 
    """
    The class that will hold the data about the player,
    and will invoke the methods of the non-human players.
    """

    players = None

    def __init__(self):
        """ Start the game and the number of the players"""
        self.players = []


    def get_player_count(self):
        """ 
        :return: int - the list of players that are currently in the game
        """
        return len(players)


    def add_new_player(self, new_player = None):
        """
        Adds a new player to the game.
        :param new_player: the new player that will be added. if the new player is not provided, a bot player will be added
        """
        raise NotImplemented("")

