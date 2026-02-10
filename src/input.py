from dataclasses import dataclass
from pgzero.keyboard import keyboard

@dataclass 
class InputState:
    left: bool = False
    right: bool = False
    jump_pressed: bool = False
    fire_pressed: bool = False
    fire_held: bool = False

class InputStateManager:
    def __init__(self):
        self.prev_fire = None
        self.prev_jump = None
    
    def build(self) -> InputState:
        state = InputState()

        state.left = keyboard.left
        state.right = keyboard.right

        state.jump_pressed = keyboard.up and not self.prev_jump
        
        state.fire_pressed = keyboard.space
        state.fire_held = keyboard.space and not self.prev_fire

        self.prev_fire = keyboard.space
        self.prev_jump = keyboard.up