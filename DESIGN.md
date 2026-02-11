# Game Design Architecture

## Screens Architecture (Task A)
We have 3 main screens:
1. `MenuScreen`: This is the screen that manages the menu and also the game is initially on this screen.
2. `PlayerScreen`: From menu screen, we transition to this screen after space is pressed, this is the screen that manages the main game such as levels
3. `GameOverScreen`: Finally, on lose condition, we transition to this screen, when player loses all lives or game is complete then this screen is shown. If player presses space, then we return back to the main screen.
4. `Screen`: This is the Base class, used as an interface

Each screen has its own `draw()` and `update()` function, which work as per requirements of each screen.

Then we have the `App` class which manages the screens and all updates for the game is passed through this object.

### Acceptance test:
1. No global state in `update()` because we use `app.update()` through `App` class.
2. `Game()` is made inside screens transition, see `MenuScreen` for initialization.
3. There exists a function in `App` for `app.change_screen(...)`.

## Input Design (Task B)
For input state, there is a dataclass in `input.py` which is built by `InputStateManager`, this is built in `app.update(...)` and it is used by the player object, menu screen and etc. The dataclass looks like:

```
@dataclass 
class InputState:
    left: bool = False
    right: bool = False
    jump_pressed: bool = False
    fire_pressed: bool = False
    fire_held: bool = False
    pause_pressed: bool = False
```

We map the specific keyboard attribute from pgzero to these input state attributes.

### Acceptance test:
1. `space_down` doesn't exist in global scope
2. `Player.update(...)` doesn't directly as access keyboard as we are passing an input state.
3. Edge detection works for both starting the game (space in menu) and firing orb (space pressed as player).

## Pause Mechanic (Task C)
When paused is pressed (on keyboard it is the key P). The game checks for the input handler (through input state) and this variable is toggled:
```
self.paused = False

...

self.paused = not self.paused
```
In `PlayerScreen.update`, if this variable is true, then all game logic is skipped but draw function works normally so everything is still there. Then in `PlayerScreen`, we check for pause and create an overlay.

### Acceptance test:
1. Pause works through `PlayerScreen` as it is implemented there.
2. Pressing pause doesn't work in menu or game over screens.
3. Game doesn't crash, everything is resumed from the same state (players, orbs, enemies, fruits)