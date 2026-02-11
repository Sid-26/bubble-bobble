from random import randint, shuffle
import pgzero
from src.game_utils import char_width, draw_text
from consts import WIDTH, CHAR_WIDTH, IMAGE_WIDTH, LEVELS, NUM_COLUMNS, GRID_BLOCK_SIZE, LEVEL_X_OFFSET, NUM_ROWS, TYPE_NORMAL, TYPE_AGGRESSIVE
from entities.robot import Robot
from entities.fruit import Fruit

class Game:
    def __init__(self):
        self.player = None
        self.level_colour = -1
        self.level = -1

        self.next_level()
    
    def next_level(self):
        self.level_colour = (self.level_colour + 1) % 4
        self.level += 1

        self.grid = LEVELS[self.level % len(LEVELS)]
        self.grid = self.grid + [self.grid[0]]

        self.timer = -1

        if self.player:
            self.player.reset()

        self.fruits = []
        self.bolts = []
        self.enemies = []
        self.pops = []
        self.orbs = []

        num_enemies = 10 + self.level
        num_strong_enemies = 1 + int(self.level / 1.5)
        num_weak_enemies = num_enemies - num_strong_enemies

        self.pending_enemies = (num_strong_enemies * [TYPE_AGGRESSIVE] + num_weak_enemies * [TYPE_NORMAL])

        shuffle(self.pending_enemies)

        self.play_sound("level", 1)
    
    def draw_text(self, text, y, x=None):
        if x == None:
            x = (WIDTH - sum([char_width(c) for c in text])) // 2

        for char in text:
            screen.blit("font0"+str(ord(char)), (x, y))
            x += char_width(char)
    
    def block(self, x, y):
        grid_x = (x - LEVEL_X_OFFSET) // GRID_BLOCK_SIZE
        grid_y = y // GRID_BLOCK_SIZE

        if grid_y > 0 and grid_y < NUM_ROWS:
            row = self.grid[grid_y]
            return (
                grid_x >= 0 and
                grid_x < NUM_COLUMNS and
                len(row) > 0 and
                row[grid_x] != " "
            )
        else:
            return False

    def draw_status(self):
        number_width = CHAR_WIDTH[0]
        s = str(self.player.score)
        draw_text(s, 451, WIDTH - 2 - (number_width * len(s)))
        draw_text("LEVEL " + str(self.level + 1), 451)

        lives_health = ["life"] * min(2, self.player.lives)
        if self.player.lives > 2:
            lives_health.append("plus")
        if self.player.lives >= 0:
            lives_health += ["health"] * self.player.health

        x = 0
        for image in lives_health:
            screen.blit(image, (x, 450))
            x += IMAGE_WIDTH[image]
            self.next_level()

    def fire_probability(self):
        return 0.001 + (0.0001 * min(100, self.level))

    def max_enemies(self):
        return min((self.level + 6) // 2, 8)

    def get_robot_spawn_x(self):
        r = randint(0, NUM_COLUMNS-1)

        for i in range(NUM_COLUMNS):
            grid_x = (r+i) % NUM_COLUMNS
            if self.grid[0][grid_x] == ' ':
                return GRID_BLOCK_SIZE * grid_x + LEVEL_X_OFFSET + 12
        return WIDTH/2

    def update(self, input_state):
        self.timer += 1
        for obj in self.fruits + self.bolts + self.enemies + self.pops + [self.player] + self.orbs:
            if obj == self.player:
                obj.update(input_state)
            else:
                obj.update()

        self.fruits = [f for f in self.fruits if f.time_to_live > 0]
        self.bolts = [b for b in self.bolts if b.active]
        self.enemies = [e for e in self.enemies if e.alive]
        self.pops = [p for p in self.pops if p.timer < 12]
        self.orbs = [o for o in self.orbs if o.timer < 250 and o.y > -40]

        if self.timer % 100 == 0 and len(self.pending_enemies + self.enemies) > 0:
            self.fruits.append(Fruit(self,(randint(70, 730), randint(75, 400))))

        if self.timer % 81 == 0 and len(self.pending_enemies) > 0 and len(self.enemies) < self.max_enemies():
            robot_type = self.pending_enemies.pop()
            pos = (self.get_robot_spawn_x(), -30)
            self.enemies.append(Robot(self, pos, robot_type))

        if len(self.pending_enemies + self.fruits + self.enemies + self.pops) == 0:
            if len([orb for orb in self.orbs if orb.trapped_enemy_type != None]) == 0:
                self.next_level()

    def draw(self):
        screen.blit("bg%d" % self.level_colour, (0, 0))
        block_sprite = "block" + str(self.level % 4)

        for row_y in range(NUM_ROWS):
            row = self.grid[row_y]
            if len(row) > 0:
                x = LEVEL_X_OFFSET
                for block in row:
                    if block != ' ':
                        screen.blit(block_sprite, (x, row_y * GRID_BLOCK_SIZE))
                    x += GRID_BLOCK_SIZE

        all_objs = self.fruits + self.bolts + self.enemies + self.pops + self.orbs
        all_objs.append(self.player)
        for obj in all_objs:
            if obj:
                obj.draw()

    def play_sound(self, name, count=1):
        if self.player:
            try:
                sound = getattr(sounds, name + str(randint(0, count - 1)))
                sound.play()
            except Exception as e:
                print(e)