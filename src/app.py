import pygame, pgzero, pgzrun, sys

class App:
    def __init__(self, screen) -> None:
        self.current_screen = screen

    def change_screen(self, next_screen):
        self.current_screen = next_screen
    
    def update(self):
        self.current_screen.update(self)
    
    def draw(self):
        self.current_screen.draw()