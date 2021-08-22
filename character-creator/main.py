class Character:
    name = "Mario"
    phrase = "It'sa me, Mario!"
    level = 1
    health = 100

    def greet(self):
        print(self.phrase)

    def level_up(self):
        self.level += 1
        print("Leveled up to: " + self.level)

    def dec_health(self):
        self.health -= 10
        print("Health has decreased to " + self.health)