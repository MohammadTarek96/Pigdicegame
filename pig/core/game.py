#!/usr/bin/env python3
# -*- coding: utf-8 -*-



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


