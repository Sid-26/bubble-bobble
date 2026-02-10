from screen import Screen
from menu import MenuScreen
from game import Game, draw_status
import pgzero

class GameOverScreen(Screen):
    def _init_(self, game):
        self.game = game
    
    def update(self, app, input_state):
        if input_state.fire_pressed:
            app.change_screen(MenuScreen(Game()))
    
    def draw(self):
        self.game.draw()
        draw_status()
        screen.blit("over", (0, 0))