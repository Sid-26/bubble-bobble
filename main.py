from src.app import App
from src.game import Game
from src.screens.menu import MenuScreen
import pgzero, pgzrun

if __name__ == "__main__":
    app = App(MenuScreen(Game()))

    def update():
        app.update()

    def draw():
        app.draw()

    pgzrun.go()

# to do for future sid, please implement the player logic here with input state (COMPLETED)
# further to do finish task C (Pause menu) (COMPLETED)
# further further to do finish documentation