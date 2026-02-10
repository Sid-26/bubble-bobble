from consts import CHAR_WIDTH, LEVEL_X_OFFSET, GRID_BLOCK_SIZE, NUM_ROWS, NUM_COLUMNS

# utility functions that dont belong to any single class
def sign(x):
    return -1 if x < 0 else 1

def char_width(char):
    index = max(0, ord(char) - 65)
    return CHAR_WIDTH[index]
