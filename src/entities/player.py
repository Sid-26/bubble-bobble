from .gravity_actor import GravityActor
from .orb import Orb
from src.consts import HEIGHT, WIDTH

class Player(GravityActor):
    def __init__(self, game):
        super().__init__(game, (0, 0))

        self.lives = 2
        self.score = 0
        self.health = 3
        self.vel_y = 0
        self.direction_x = 1
        self.fire_timer = 0
        self.hurt_timer = 100
        self.blowing_orb = None

    def reset(self):
        self.pos = (WIDTH / 2, 100)
        self.vel_y = 0
        self.direction_x = 1            # -1 = left, 1 = right
        self.fire_timer = 0
        self.hurt_timer = 100   # Invulnerable for this many frames
        self.health = 3
        self.blowing_orb = None

    def hit_test(self, other):
        if self.collidepoint(other.pos) and self.hurt_timer < 0:
            self.hurt_timer = 200
            self.health -= 1
            self.vel_y = -12
            self.landed = False
            self.direction_x = other.direction_x
            if self.health > 0:
                self.game.play_sound("ouch", 4)
            else:
                self.game.play_sound("die")
            return True
        else:
            return False

    def update(self, input_state):
        super().update(self.health > 0)

        self.fire_timer -= 1
        self.hurt_timer -= 1

        if self.landed:
            self.hurt_timer = min(self.hurt_timer, 100)

        if self.hurt_timer > 100:
            if self.health > 0:
                self.move(self.direction_x, 0, 4)
            else:
                if self.top >= HEIGHT*1.5:
                    self.lives -= 1
                    self.reset()
        else:
            dx = 0
            if input_state.left:
                dx = -1
            elif input_state.right:
                dx = 1

            if dx != 0:
                self.direction_x = dx


                if self.fire_timer < 10:
                    self.move(dx, 0, 4)

            if  input_state.fire_pressed and self.fire_timer <= 0 and len(self.game.orbs) < 5:
                x = min(730, max(70, self.x + self.direction_x * 38))
                y = self.y - 35
                self.blowing_orb = Orb(self.game, (x,y), self.direction_x)
                self.game.orbs.append(self.blowing_orb)
                self.game.play_sound("blow", 4)
                self.fire_timer = 20

            if input_state.jump_pressed and self.vel_y == 0 and self.landed:
                self.vel_y = -16
                self.landed = False
                self.game.play_sound("jump")

        # Holding down space causes the current orb (if there is one) to be blown further
        if input_state.fire_held:
            if self.blowing_orb:
                # Increase blown distance up to a maximum of 120
                self.blowing_orb.blown_frames += 4
                if self.blowing_orb.blown_frames >= 120:
                    # Can't be blown any further
                    self.blowing_orb = None
        else:
            # If we let go of space, we relinquish control over the current orb - it can't be blown any further
            self.blowing_orb = None

        # Set sprite image. If we're currently hurt, the sprite will flash on and off on alternate frames.
        self.image = "blank"
        if self.hurt_timer <= 0 or self.hurt_timer % 2 == 1:
            dir_index = "1" if self.direction_x > 0 else "0"
            if self.hurt_timer > 100:
                if self.health > 0:
                    self.image = "recoil" + dir_index
                else:
                    self.image = "fall" + str((self.game.timer // 4) % 2)
            elif self.fire_timer > 0:
                self.image = "blow" + dir_index
            elif dx == 0:
                self.image = "still"
            else:
                self.image = "run" + dir_index + str((self.game.timer // 8) % 4)
