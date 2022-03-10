#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Defines the shell class, that handles the user input.

The game is split between two interfaces:
Start game menu, with the options to start a new game and exit
A game menu, that will handle the input while in-game
"""
import cmd
from core.game import Game
from core.player import HumanPlayer


class MainMenuShell(cmd.Cmd):
    """
    Greets the player, and guides him through to starting the game
    """
    intro = "Welcome to the game! Type help or ? to list commands. \n"
    prompt = "(PigGame)> "
    game = None
    player_name = None
    player_instance = None

    def __init__(self):
        """Initialize the menu"""
        super().__init__()
        self.game = Game()
        
        self.player_name = input("Hello. What is your name?> ")
        self.player_instance = HumanPlayer(self.player_name)
        self.game.add_new_player(self.player_instance)

    def do_start(self, _):
        """Starts the game, and launches the game shell"""
        msg = "Your game will now start. Good luck!"
        return True

    def do_add(self, _):
        raise NotImplemented("This function has yet to be implemented")

    def do_change(self, arg):
        """
        Command that allows the player to change params related to the game.
        :param arg: the option specifing what to change. 
            "name" - change the player name
        """
        if arg.lower() == "name":
            self.player_name = input("(New name) ")
            self.player_instance.change_name(self.player_name)
        else:
            print(f"at the momment, you cannot change {arg}")

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



