#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Defines the shell class, that handles the user input.

The game is split between two interfaces:
Start game menu, with the options to start a new game and exit
A game menu, that will handle the input while in-game
"""
import cmd
from game import Game
from player import HumanPlayer
from exceptions import TooManyPlayersError


class MainMenuShell(cmd.Cmd):
    """Greets the player, and guides him through to starting the game."""

    intro = "Welcome to the game! Type help or ? to list commands. \n"
    prompt = "(PigGameMenu)> "
    game = None
    player_name = None
    player_instance = None

    def __init__(self):
        """Initialize the menu."""
        super().__init__()
        self.reset_game()

    def reset_game(self):
        """Reset the game, and creates the first player."""
        self.game = Game()
        # adds the player to the game
        self.player_name = input("Hello. What is your name?> ")
        self.player_instance = HumanPlayer(self.player_name)
        self.game.add_new_player(self.player_instance)

    def do_start(self, _):
        """Start the game, and launches the game shell."""
        print("Your game will now start. Good luck!")
        # passing a list will be a pass-by-reference
        # and any modifications done will be usable here
        quit_helper = [False]
        GameShell(self.game, quit_helper).cmdloop()
        if not quit_helper[0]:
            self.reset_game()
        return quit_helper[0]

    def do_add(self, arg):
        """
        Add a new player to the game.

        Requires an argument, for example: add bot
        argument values:
            bot: adds a new bot
            player: adds a new player

        Some say the game is more fun with more players!
        """
        if arg == "":
            print("You need to provide an argument."
                  "Type '? add' for more information")
        elif arg == "bot":
            try:
                new_player = self.game.add_new_player()
                print(f"New player added. Let's welcome {new_player.name}"
                      f"to the table! \n There are "
                      f"{self.game.get_player_count()}"
                      f"player(s) at the table!")
            except TooManyPlayersError:
                print("All the game slots are full! type "
                      "[start] to start the game!")
        elif arg == "player":
            try:
                new_player_name = input("\t(PlayerName)>")
                new_player = self.game.add_new_player(HumanPlayer(
                    new_player_name))
                print(f"New player added. Let's welcome {new_player.name}"
                      f"to the table! \n"
                      f"There are {self.game.get_player_count()} player(s)"
                      f"at the table!")
            except TooManyPlayersError:
                print("All the game slots are full! type [start]"
                      "to start the game!")

    # all commands related to the quit & alias
    def do_exit(self, _):
        """Quit the game."""
        print("Until next time. Bye!")
        return True

    def do_quit(self, arg):
        """Alias command for exit."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Alias command for exit."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Will end the game due to end of input."""
        return self.do_exit(arg)


class GameShell(cmd.Cmd):
    """
    Handles the input while in-game.

    Commands available:
    ! end-restart
    - end/q/quit/EOF
    - restart

    ! game commands
    - roll
    - end turn/pass

    ! immoral but
    - roll [a loaded dice {points}]
    - cheat
    """

    intro = "Your turn. Type ? or help to list all the commands"
    prompt = "(PigGame)>"
    game = None

    def __init__(self, game, quit_helper):
        """Initialize the menu."""
        super().__init__()
        self.game = game
        self.quit_helper = quit_helper
        self.reset_prompt()

    def reset_prompt(self):
        """Change the prompt to use the current player's name."""
        player_name = self.game.players[self.game.turn].name
        self.prompt = f"(PigGame {player_name}'s turn) > "

    # game handlers
    def do_roll(self, arg):
        """Roll [arg]*.

        missing arg - roll a normal roll
        'a loaded dice {number}' - cheats for the player with the value
            indicated
        """
        if arg == "":
            self.game.roll_for_current_player()
        elif arg.lower().startswith("a loaded dice"):
            try:
                self.game.cheat_for_current_player(
                    int(arg[len("a loaded dice"):].strip())
                )
            except ValueError:
                print(f"I cannot cheat for {arg}")
        self.reset_prompt()

    def do_end(self, arg):
        """End [arg].

        - g/game: ends the game. Alias for exit
        - t/turn: ends the turn. Alias for pass
        """
        if arg == "":
            print("end requires an additional argument.Type '? end' for help")
            return False
        if arg.lower() in ["t", "turn"]:
            return self.do_pass("")
        if arg.lower() in ["g", "game"]:
            return self.do_exit("")
        print("argument not recognized. Type '? end' for a list "
              "of possible arguments")
        return False

    def do_pass(self, _):
        """Pass, ends the turn for the player."""
        self.game.end_turn_for_current_player()
        self.reset_prompt()
        if self.game.game_ended:
            print("The game ended. Hopefully, you had fun!"
                  "See you in another game?")
            return self.do_restart(_)
        return False

    def do_cheat(self, arg):
        """Add however many points typed to the current player's score.

        Command format:
        Cheat [points].
        """
        try:
            self.game.cheat_for_current_player(int(arg.strip()))
        except ValueError:
            print(f"I cannot cheat for {arg}")

    # game commands
    def do_restart(self, _):
        """Return to the main menu, and lets you configure a new game."""
        return True

    def do_q(self, _):
        """End the game, alias for exit."""
        return self.do_exit(_)

    def do_quit(self, _):
        """End the game, alias for exit."""
        return self.do_exit(_)

    def do_EOF(self, _):
        """End the game, when there is no more input."""
        return self.do_exit(_)

    def do_exit(self, _):
        """End the game, alias for exit."""
        self.quit_helper[0] = True
        return True
