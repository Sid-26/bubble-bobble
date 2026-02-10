from collide_actor import CollideActor
from consts import ANCHOR_CENTRE_BOTTOM, HEIGHT
from game_utils import sign

class GravityActor(CollideActor):
    MAX_FALL_SPEED = 10

    def __init__(self, game, pos):
        super().__init__(game, pos, ANCHOR_CENTRE_BOTTOM)

        self.vel_y = 0
        self.landed = False

    def update(self, detect=True):
        self.vel_y = min(self.vel_y + 1, GravityActor.MAX_FALL_SPEED)

        if detect:
            if self.move(0, sign(self.vel_y), abs(self.vel_y)):
                self.vel_y = 0
                self.landed = True

            if self.top >= HEIGHT:
                self.y = 1
        else:
            self.y += self.vel_y