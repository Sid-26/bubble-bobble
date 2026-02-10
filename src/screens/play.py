from screen import Screen
from game_over import GameOverScreen

class PlayerScreen(Screen):
    def __init__(self, game):
        self.game = game
    
    def update(self, app):
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            app.change_screen(GameOverScreen(self.game))
        else:
            self.game.update()
    
    def draw(self):
        self.game.draw()
        self.game.draw_status()

    def draw_status(self):
        pass