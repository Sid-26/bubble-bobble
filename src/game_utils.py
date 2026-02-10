from consts import CHAR_WIDTH, LEVEL_X_OFFSET, GRID_BLOCK_SIZE, NUM_ROWS, NUM_COLUMNS

# utility functions that dont belong to any single class
def sign(x):
    return -1 if x < 0 else 1

def char_width(char):
    index = max(0, ord(char) - 65)
    return CHAR_WIDTH[index]

def block(self, x,y):
    # Is there a level grid block at these coordinates?
    grid_x = (x - LEVEL_X_OFFSET) // GRID_BLOCK_SIZE
    grid_y = y // GRID_BLOCK_SIZE

    if grid_y > 0 and grid_y < NUM_ROWS:
        row = self.grid[grid_y]
        return grid_x >= 0 and grid_x < NUM_COLUMNS and len(row) > 0 and row[grid_x] != " "
    else:
        return False