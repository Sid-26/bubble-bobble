from screen import Screen
from game import Game
from entities.player import Player
from play import PlayerScreen
import pgzero

class MenuScreen(Screen):
    def __init__(self, game):
        self.game = game
    
    def update(self, app, input_state):
        if input_state.fire_pressed:
            new_game = Game()
            player = Player(new_game)
            new_game.player = player
            
            app.change_screen(PlayerScreen(new_game))
        else:
            self.game.update()
    
    def draw(self):
        self.game.update()
        screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))