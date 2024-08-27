import pygame
from main_file import GameMainWindow


class StartingWindow(GameMainWindow):
    def __init__(self):
        super().__init__()

    def update(self):
        self.check_events()
