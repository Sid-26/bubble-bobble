from .screen import Screen

from pygame import Rect
from src.consts import HEIGHT, WIDTH

class PlayerScreen(Screen):
    def __init__(self, game):
        self.game = game
        self.paused = False
    
    def update(self, app, input_state):
        if input_state.pause_pressed:
            self.paused = not self.paused
            return
        
        if self.paused:
            return

        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from .game_over import GameOverScreen
            app.change_screen(GameOverScreen(self.game))
        else:
            self.game.update(input_state)
    
    def draw(self):
        self.game.draw()
        self.game.draw_status()

        if self.paused:
            screen.draw.filled_rect(
                Rect((0, 0), (WIDTH, HEIGHT)),
                (0, 0, 0, 150)
            )

            self.game.draw_text("PAUSED", HEIGHT // 2)

    def draw_status(self):
        pass