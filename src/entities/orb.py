from .collide_actor import CollideActor
from .fruit import Fruit
from .pop import Pop
from random import randint

class Orb(CollideActor):
    MAX_TIMER = 250

    def __init__(self, game, pos, dir_x):
        super().__init__(game, pos)

        # Orbs are initially blown horizontally, then start floating upwards
        self.direction_x = dir_x
        self.floating = False
        self.trapped_enemy_type = None      # Number representing which type of enemy is trapped in this bubble
        self.timer = -1
        self.blown_frames = 6  # Number of frames during which we will be pushed horizontally

    def hit_test(self, bolt):
        # Check for collision with a bolt
        collided = self.collidepoint(bolt.pos)
        if collided:
            self.timer = Orb.MAX_TIMER - 1
        return collided

    def update(self):
        self.timer += 1

        if self.floating:
            # Float upwards
            self.move(0, -1, randint(1, 2))
        else:
            # Move horizontally
            if self.move(self.direction_x, 0, 4):
                # If we hit a block, start floating
                self.floating = True

        if self.timer == self.blown_frames:
            self.floating = True
        elif self.timer >= Orb.MAX_TIMER or self.y <= -40:
            # Pop if our lifetime has run out or if we have gone off the top of the screen
            self.game.pops.append(Pop(self.game, self.pos, 1))
            if self.trapped_enemy_type != None:
                # trapped_enemy_type is either zero or one. A value of one means there's a chance of creating a
                # powerup such as an extra life or extra health
                self.game.fruits.append(Fruit(self.game, self.pos, self.trapped_enemy_type))
            self.game.play_sound("pop", 4)

        if self.timer < 9:
            # Orb grows to full size over the course of 9 frames - the animation frame updating every 3 frames
            self.image = "orb" + str(self.timer // 3)
        else:
            if self.trapped_enemy_type != None:
                self.image = "trap" + str(self.trapped_enemy_type) + str((self.timer // 4) % 8)
            else:
                self.image = "orb" + str(3 + (((self.timer - 9) // 8) % 4))