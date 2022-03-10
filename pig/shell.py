#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Defines the shell class, that handles the user input.

The game is split between two interfaces:
Start game menu, with the options to start a new game and exit
A game menu, that will handle the input while in-game
"""
import cmd
from pig.core.game import Game


class MainMenuShell(cmd.Cmd):
    """
    Greets the player, and guides him through to starting the game
    """
    intro = "Welcome to the game! Type help or ? to list commands. \n"
    prompt = "(PigGame)> "
    game = None

    def __init__(self):
        """Initialize the menu"""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        """Starts the game, and launches the game shell"""
        msg = "Your game will now start. Good luck!"
        return True

    def do_add(self, _):
        print("Currently, there are: {}".format(self.game.get_player_count())
        raise NotImplemented("This function has yet to be implemented")


    # all commands related to the quit & alias
    def do_exit(self, _):
        """Player has chosen to end the game."""
        print("Until next time. Bye!")
        return True

    def do_quit(self, arg):
        """Alias command for exit"""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Alias command for exit"""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Ended due to no more input Ctrl+Z (win) / Ctrl+D (bash)"""
        return self.do_exit(arg)


class GameShell(cmd.Cmd):
    """
    Handles the input while in-game.
    Commands available:
    - end/q/quit/EOF
    - roll
    - end_turn/pass

    ! immoral, but
    - CHEAT
    """
    intro = "Your turn. Type ? or help to list all the commands"
    prompt = "(PigGame> )"
    game = None

    def __init__(self, game):
        """Initialize the menu"""
        super.__init__()
        self.game = game



