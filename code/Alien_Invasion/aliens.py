import pygame
from pygame.sprite import Sprite
from setting import Setting

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Setting instance
        self.setting = ai_game.setting

        # Load Alien Image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Position of Alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Changing position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.rect.x += (self.setting.alien_speed 
                    * self.setting.fleet_direction)


        
