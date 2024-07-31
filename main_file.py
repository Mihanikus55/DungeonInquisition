import sys

import json
import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.load_settings()

        self.screen = pygame.display.set_mode(
            (self.game_settings["screen_width"], self.game_settings["screen_height"]))

        pygame.display.set_caption(self.game_settings["caption"])

        # pygame.display.set_icon(self.game_settings.icon)

        self.fpsClock = pygame.time.Clock()

    def load_settings(self):
        with open("settings.json", encoding='utf-8') as f:
            settings = json.load(f)
            self.game_settings = settings["game"]
            self.default_settings = settings["default"]

    def set_default_settings(self):
        for key, value in self.default_settings.items():
            if key in self.game_settings:
                self.game_settings[key] = value

    def run(self):
        while True:
            self.check_events()

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.fpsClock.tick(self.game_settings["fps"])

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()

    def save_game(self):
        self.save_settings()

    def save_settings(self):
        with open("settings.json", "w") as f:
            f.write(json.dumps({"game": self.game_settings, "default": self.default_settings}))

    def quit_game(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    de = Game()
    de.run()
