import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self):
        super().__init__()
        # Load image
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height