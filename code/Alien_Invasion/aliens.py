import pygame
from pygame.sprite import Sprite
from setting import Setting

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Setting instance
        self.setting = Setting()

        # Load Alien Image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Position of Alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Changin position
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.setting.alien_speed 
                    * self.setting.fleet_direction)

        self.rect.x = self.x

        
