from entities.collide_actor import CollideActor

class Bolt(CollideActor):
    SPEED = 7

    def __init__(self, game, pos, dir_x):
        super().__init__(game, pos)

        self.direction_x = dir_x
        self.active = True

    def update(self):
        if self.move(self.direction_x, 0, Bolt.SPEED):
            # Collided
            self.active = False
        else:
            for obj in self.game.orbs + [self.game.player]:
                if obj and obj.hit_test(self):
                    self.active = False
                    break

        direction_idx = "1" if self.direction_x > 0 else "0"
        anim_frame = str((self.game.timer // 4) % 2)
        self.image = "bolt" + direction_idx + anim_frame