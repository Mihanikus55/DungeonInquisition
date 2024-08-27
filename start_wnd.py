import pygame


class StartingWindow:
    def __init__(self, settings, screen):
        self.game_settings = settings
        self.screen = screen

        self.game_settings["cur_bg"] = pygame.transform.scale(
            pygame.image.load('game_data/backgrounds/starting_bg.png'),
            (self.game_settings["screen_width"],
             self.game_settings["screen_height"]))

    def update(self):
        self.screen.blit(self.game_settings["cur_bg"], (0, 0))
