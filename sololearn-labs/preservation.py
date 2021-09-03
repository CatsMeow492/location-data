class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        if (self._lives <= 1):
            print("Game Over")
        else:
            self._lives -= 1
            print(self._lives)
        

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()