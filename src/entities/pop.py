from pgzero.builtins import Actor

class Pop(Actor):
    def __init__(self, game, pos, type):
        super().__init__("blank", game, pos)

        self.type = type
        self.timer = -1

    def update(self):
        self.timer += 1
        self.image = "pop" + str(self.type) + str(self.timer // 2)