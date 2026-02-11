from .screen import Screen
from src.game import Game
from src.entities.player import Player

class MenuScreen(Screen):
    def __init__(self, game):
        self.game = game
    
    def update(self, app, input_state):
        if input_state.fire_pressed:
            from .play import PlayerScreen
            new_game = Game()
            player = Player(new_game)
            new_game.player = player
            app.change_screen(PlayerScreen(new_game))
        else:
            self.game.update(input_state)
    
    def draw(self, screen):
        self.game.draw(screen)
        screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))