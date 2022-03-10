

class Player:
    score = 0
    current_turn_score = 0

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"<{self.name}, score: {self.score}>"

    def finish_turn(self):
        self.score += self.current_turn_score
        self.current_turn_score = 0

class HumanPlayer(Player):
    pass


class BotPlayer(Player):
    pass

