import sys

import json
import pygame
from pygame.locals import *
from ctypes import windll

from start_wnd import StartingWindow


class GameMainWindow:
    def __init__(self):
        pygame.init()
        self.load_settings()
        self.load_display_wh()
        self.set_display_mode()

        self.change_cur_wnd(StartingWindow(self.game_settings, self.screen))

        self.fpsClock = pygame.time.Clock()

    def load_display_wh(self):
        self.user32 = windll.user32
        self.user32.SetProcessDPIAware()
        width = self.user32.GetSystemMetrics(0)
        height = self.user32.GetSystemMetrics(1)
        self.game_settings["screen_width"] = width
        self.game_settings["screen_height"] = height
        self.save_settings()

    def set_display_mode(self):
        self.screen = pygame.display.set_mode(
            (self.game_settings["screen_width"], self.game_settings["screen_height"]))

        pygame.display.set_caption(self.game_settings["caption"])
        # pygame.display.set_icon(self.game_settings.icon)

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
            self.screen.fill((0, 0, 0))

            self.check_events()
            self.cur_window.update()
            pygame.display.flip()
            self.fpsClock.tick(self.game_settings["fps"])

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()

    def change_cur_wnd(self, name_wnd):
        self.cur_window = name_wnd

    def save_game(self):
        self.save_settings()

    def save_settings(self):
        with open("settings.json", "w") as f:
            f.write(json.dumps({"game": self.game_settings, "default": self.default_settings}))

    def quit_game(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    de = GameMainWindow()
    de.run()
