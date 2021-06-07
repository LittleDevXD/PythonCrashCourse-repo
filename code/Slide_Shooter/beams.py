import pygame
from pygame.sprite import Sprite

class Beam(Sprite):
    """ Beam class inherited from Sprite """
    def __init__(self, game):
        super().__init__()

        # Screen
        self.screen = game.screen

        # Setting instance
        self.setting = game.setting

        # Shooter instance
        self.shooter_rect = game.shooter.shooter_rect

        # Beam rect
        self.beam_rect = pygame.Rect(0, 0, 
                            self.setting.beam_width, self.setting.beam_height)

        # Positon
        self.beam_rect.midleft = self.shooter_rect.midleft

        # Speed
        self.speed = self.setting.beam_speed
        self.x = float(self.beam_rect.x)

        # Color
        self.color = self.setting.beam_color

    def update(self):
        """ Update the position of the bullet """
        self.x -= self.speed
        self.beam_rect.x = self.x

    def draw_bullet(self):
        """ Draw new bullet """
        pygame.draw.rect(self.screen, self.color, self.beam_rect)
