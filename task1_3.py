class Titandex():
    def __init__(self, name, height, strength, winning_streak = 0 ):
        self.name = name
        self.height = height
        self.strength = strength
        self.winning_streak = winning_streak

    def TitanvsScout(self,scout_name, scout_strength):
        if self.strength > scout_strength:
            print(self.name,"is the winner")
            self.winning_streak += 1
        elif self.strength == scout_strength:
            print("Draw")
        else:
            print(scout_name,"is the winner")
            self.winning_streak = 0

    def TitanvsTitan(self,titan_name, titan_strength):
        if self.name == titan_name:
            print("Titan can not fight with itself")
        elif self.strength > titan_strength:
            print(self.name,"is the winner")
            self.winning_streak += 1
        elif self.strength == titan_strength:
            print("Draw")
        else:
            print(titan_name,"is the winner")
            self.winning_streak = 0
