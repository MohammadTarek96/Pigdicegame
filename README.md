Pig Dice Game 
==========================
developed by Mohammad Tarek Housary, Kotyba sayed. 

Basics of the game
-------------------

we have decided to limit the game to 4 players 
who can be either be bots or actual users. 

the game can be played by a single player up to 4 playres. 

to add a human player enter: add player 
to add a bot enter: add bot

actual Users can enter their names. 

players will enter: roll to roll the dice till they roll a 1, or decide to pass.

by rolling a 1 the player turn will end and he will not carry his score to the next turn 
by entering: pass the player will end his turn and carry his score forward. 

all players are meant to play the same amount of turns. 

tha last turn is when someone reaches or crosses 100 points. 

there could be multiple winners, if multiple players finish the last turn
with the same exact amount of points. 

the user is able to access a list of commands (help) by entering ? or help at anytime 

the user is able to restart or exit the current game during the actual gameplay. 

the user can Cheat to reach the end of the game quickly by entering Cheat x
when x is a number of points for example: Cheat 50 
the user will be awarded 50 points to add to his current score. 

bots players have three different stratgies (Playstyles). 
a bot will randomly be set to one of them. 
low risk: will pass turn on reaching 6 points 
meduim risk: will pass turn on reaching 12 points 
high risk: will pass turn on reaching 18 points.


list of the gameplay commands:
------------------------------
? > list of commands. 

help > list of commands.

add player > to add a human player. 

add bot > to add a a bot player. 

roll > to roll the die. 

pass > to end turn and keep your score.

Cheat > to add extra points to your turn without rolling the dice

restart > to resatrt the game.

q > to quit the game.

This game was developed in a TDD enviroment.
----------------------------------------------------------------------------------
The next will be a list of commands to run the game in the terminal, how to install the requiermnts to run the project development enviroment,
unittest the code, generate documentation, generate UML diagrams, for more look into the makefile! 

Get going and Run the game
--------------------------

This is how you can work with the development environment.

### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```


### Run the code

the game can be started like this.

provide the path of the game folder 
in your terminal 

for example if you are using git bash terminal 

$ cd Downloads\Pigdicegame-main\Pigdicegame-main

this may differe on your machine so manually get the correct path 

```
# Execute the main program
python pig/main.py
```

All code is stored below the directory `pig/`. 

Get going and setup the development enviroment 
----------------------------------------------

### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```


### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `guess/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

#### Generating documintation and UML diagrams

```
# Generate documintation for the project 
make pydoc 
```
```
# Generate UML diagrams 
make 
```

### Remove generated files

You can remove all generated files by this.
```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```
