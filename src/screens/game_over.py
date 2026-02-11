from .screen import Screen
from src.game import Game
from pgzero.builtins import screen

class GameOverScreen(Screen):
    def _init_(self, game):
        self.game = game
    
    def update(self, app, input_state):
        if input_state.fire_pressed:
            from .menu import MenuScreen
            app.change_screen(MenuScreen(Game()))
    
    def draw(self, screen):
        self.game.draw(screen)
        self.game.draw_status(screen)
        screen.blit("over", (0, 0))