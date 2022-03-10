#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game of pig dice.

You against yourself or other (up to 4) computers, will take turns throwing the dice.
Each turn, you are allowed to either throw or pass.
If you throw a 1, you get 0 points, and your turn ends.
If you throw 2-6, you get the number of points thrown added to the turn score
If you pass, you get the turn score added to your total score.

First to 100 points wins! Good luck!
"""

import shell

def main():
    """Start the game by invoking the command loop"""
    print(__doc__) # prints the text defined above
    shell