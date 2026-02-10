from screen import Screen
from game import Game, Player
from play import PlayerScreen
import pgzero

class MenuScreen(Screen):
    def __init__(self, game):
        self.game = game
    
    def update(self, app, input_state):
        if input_state.fire_pressed:
            new_game = Game(Player())
            app.change_screen(PlayerScreen(new_game))
        else:
            self.game.update()
    
    def draw(self):
        self.game.update()
        screen.blit("title", (0, 0))

        # Draw "Press SPACE" animation, which has 10 frames numbered 0 to 9
        # The first part gives us a number between 0 and 159, based on the game timer
        # Dividing by 4 means we go to a new animation frame every 4 frames
        # We enclose this calculation in the min function, with the other argument being 9, which results in the
        # animation staying on frame 9 for three quarters of the time. Adding 40 to the game timer is done to alter
        # which stage the animation is at when the game first starts
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))