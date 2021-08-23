class Archer:
    arrows = 10
    points = 0
    empty = False

    def shoot(self):
        if self.arrows >= 1:
            print("Aim .... and shoot!")
            self.arrows -= 1
        else:
            self.empty = True

    def bullseye(self):
        self.points += 3

    def reload(self):
        if self.empty == True:
                self.arrows = 10
                self.empty = False

me = Archer()
me.shoot()
me.bullseye()
print(me.points)

        