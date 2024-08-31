import pygame
from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(self, screen, settings, buttons, rect, button_text="", image=None):
        super().__init__(buttons)
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont('Arial', 40)
        self.button_text = self.font.render(button_text, True, (20, 20, 20))
        self.image = image
        self.rect = rect
        self.button_surface = pygame.Surface((rect.width, rect.height))

        self.color = (100, 100, 100)

        self.btn_pressed = False

        if image:
            self.image = pygame.transform.scale(pygame.image.load(image), (rect.width, rect.height))

    def pressed(self):
        self.btn_pressed = True
        self.time_btn = 0
        self.color = (50, 50, 50)

    def check_collide(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = (125, 125, 125)
        else:
            self.color = (100, 100, 100)

    def update(self):
        if self.btn_pressed:
            self.time_btn += 1
            if self.time_btn == self.settings["time_button_pressed"]:
                self.btn_pressed = False
        else:
            self.check_collide(pygame.mouse.get_pos())

        if self.image:
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            self.button_surface.fill(self.color)
            self.button_surface.blit(self.button_text, [
                self.rect.width / 2 - self.button_text.get_rect().width / 2,
                self.rect.height / 2 - self.button_text.get_rect().height / 2
            ])
            self.screen.blit(self.button_surface, (self.rect.x, self.rect.y))