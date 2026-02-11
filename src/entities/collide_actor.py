from src.consts import ANCHOR_CENTRE, GRID_BLOCK_SIZE
from pgzero.actor import Actor

class CollideActor(Actor):
    def __init__(self, game, pos, anchor=ANCHOR_CENTRE):
        super().__init__("blank", pos, anchor)
        self.game = game

    def move(self, dx, dy, speed):
        new_x, new_y = int(self.x), int(self.y)

        # Movement is done 1 pixel at a time, which ensures we don't get embedded into a wall we're moving towards
        for i in range(speed):
            new_x, new_y = new_x + dx, new_y + dy

            if new_x < 70 or new_x > 730:
                # Collided with edge of level
                return True


            if ((dy > 0 and new_y % GRID_BLOCK_SIZE == 0 or
                 dx > 0 and new_x % GRID_BLOCK_SIZE == 0 or
                 dx < 0 and new_x % GRID_BLOCK_SIZE == GRID_BLOCK_SIZE-1)
                and self.game.block(new_x, new_y)):
                    return True

            # We only update the object's position if there wasn't a block there.
            self.pos = new_x, new_y

        # Didn't collide with block or edge of level
        return False