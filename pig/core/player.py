

class Player:
    name: str
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

class HumanPlayer(Player):
    pass

class BotPlayer(Player):
    pass

