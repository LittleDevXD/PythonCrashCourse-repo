import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.ship = ai_game.ship

        # Starting position of bullet
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = self.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # update the bullet position
        self.y -= self.setting.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullets on screen
        pygame.draw.rect(self.screen, self.setting.bullet_color, self.rect)
