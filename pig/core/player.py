

class Player:
    name: str
    score: int

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"<{self.name}, score: {self.score}>"

class HumanPlayer(Player):
    current_turn_score: int
    def __init__(self, name):
        super().__init__(name)
        self.current_turn_score = 0

    def finish_turn(self):
        self.score += self.current_turn_score
        self.current_turn_score = 0


class BotPlayer(Player):
    pass

