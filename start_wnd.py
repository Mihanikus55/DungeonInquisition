import pygame
from button import Button


class StartingWindow:
    def __init__(self, settings, screen):
        self.game_settings = settings
        self.screen = screen

        self.play_button = pygame.Rect(self.game_settings["screen_width"] / 2 - 100,
                                       self.game_settings["screen_height"] - self.game_settings["screen_height"] / 2.6,
                                       225, 75)
        self.settings_button = pygame.Rect(self.play_button.x, self.play_button.y + self.play_button.height + 20, 225, 75)

        self.buttons = pygame.sprite.Group()
        self.create_buttons()

        self.game_settings["cur_bg"] = pygame.transform.scale(
            pygame.image.load('game_data/backgrounds/starting_bg.png'),
            (self.game_settings["screen_width"],
             self.game_settings["screen_height"]))

    def create_buttons(self):
        Button(self.screen, self.game_settings, self.buttons, self.play_button, "PLAY")
        Button(self.screen, self.game_settings, self.buttons, self.settings_button, "SETTINGS")

    def check_buttons_clicked(self, mouse_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.pressed()

    def update(self):
        self.buttons.update()
