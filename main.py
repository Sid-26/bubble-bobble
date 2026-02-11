print("checking if imports")
from src.app import App
from src.game import Game
from src.screens.menu import MenuScreen
import pgzero, pgzrun

print("just before main")
# if __name__ == "__main__":
print("trying to run main")
app = App(MenuScreen(Game()))

def update():
    app.update()

def draw():
    app.draw()

try:
    pgzrun.go()
    print("finished running")
except Exception as e:
    print(f"Fatal Error: {e}")
    import traceback
    traceback.print_exc()

# to do for future sid, please implement the player logic here with input state (COMPLETED)
# further to do finish task C (Pause menu) (COMPLETED)
# further further to do finish documentation