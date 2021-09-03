class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


player = Player(input(), input())
player.intro()

# Code is meant to construct a player class based on user inputs.  Then call a method to introduce the player

