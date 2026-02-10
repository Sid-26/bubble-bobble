import pygame, pgzero, pgzrun
from input import InputStateManager

class App:
    def __init__(self, screen) -> None:
        self.current_screen = screen
        self.input_state_manager = InputStateManager()

    def change_screen(self, next_screen):
        self.current_screen = next_screen
    
    def update(self):
        input_state = self.input_state_manager.build()
        self.current_screen.update(self, input_state)
    
    def draw(self):
        self.current_screen.draw()