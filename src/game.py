from random import randint, shuffle

class Game:
    def block(self, x,y):
        # Is there a level grid block at these coordinates?
        grid_x = (x - LEVEL_X_OFFSET) // GRID_BLOCK_SIZE
        grid_y = y // GRID_BLOCK_SIZE

        if grid_y > 0 and grid_y < NUM_ROWS:
            row = self.grid[grid_y]
            return grid_x >= 0 and grid_x < NUM_COLUMNS and len(row) > 0 and row[grid_x] != " "
        else:
            return False

class Player:
    pass

# utils
def sign(x):
    # Returns -1 or 1 depending on whether number is positive or negative
    return -1 if x < 0 else 1
