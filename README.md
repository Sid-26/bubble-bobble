# Bubble Bobble
Interactive Media Assignment Winter 2026

This assignment is based on refactoring an existing game. The refactored game is based on: https://github.com/Wireframe-Magazine/Code-the-Classics/tree/master/cavern-master

## How to run game
1. Setup a python virtual environment 
```
python -m venv venv
/venv/Scripts/activate
```
2. `pip install pgzero`
3. `python main.py`

## How to run tests
Press P to pause


## Summary of architecture
The project architecture is divided into screens, entities and others. We also have a main.py that acts as the starting point for running the game. In `app.py`, we have the `App` class, which manages the screens and input states. Then we have entities which includes actors such as fruits, robots (enemies) and the player. Then we have screens, screens are divided into `MenuScreen`, `PlayerScreen` and `GameOverScreen`. Then in `game.py` , we manage the game logic from the original game, wrapped in a `Game` class. In `input.py`, the game manages the input state that is passed to the player object. Moreover there is a pause feature implemented as an overlay in `PlayerScreen`.
```
.
├── images/
├── music
├── sounds/
├── src/
│   ├── entities/
│   ├── screens/
│   ├── app.py
│   ├── game.py
│   ├── input.py
│   ├── consts.py
│   └── game_utils.py
└── main.py
```

> Note: Please see [DESIGN.md](DESIGN.md) to see more detailed architecture refactoring changes from the main game 