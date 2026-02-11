print("checking if imports")
from src.app import App
from src.game import Game
from src.screens.menu import MenuScreen
from src.consts import HEIGHT, WIDTH, TITLE
import pgzero, pgzrun

# print("just before main")

print("trying to run main")
app = App(MenuScreen(Game()))

def update():
    app.update()

def draw():
    app.draw(screen)
    
# if __name__ == "__main__":
try:
    pgzrun.go()
    print("finished running")
except Exception as e:
    print(f"Fatal Error: {e}")
    import traceback
    traceback.print_exc()
