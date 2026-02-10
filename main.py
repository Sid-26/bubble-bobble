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