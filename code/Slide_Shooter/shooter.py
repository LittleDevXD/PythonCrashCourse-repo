import pygame
from settings import Setting

class Shooter:
    def __init__(self, game):
        # Screen of game
        self.game = game.screen
        self.game_rect = self.game.get_rect()

        # Image of shooter
        self.shooter = pygame.image.load('images/shooter.png')
        self.shooter_rect = self.shooter.get_rect()

        # Setting instance
        self.setting = Setting()

        # Position
        self.shooter_rect.midright = self.game_rect.midright

        # Speed
        self.speed = self.setting.shooter_speed
        self.y = float(self.shooter_rect.y)

        # Flags to change speed
        self.move_up = False
        self.move_down = False

    def blitme(self):
        self.game.blit(self.shooter, self.shooter_rect)

    def update(self):
        if self.move_up and self.shooter_rect.top > 0:
            self.y -= self.speed
        elif self.move_down and self.shooter_rect.bottom < self.game_rect.bottom:
            self.y += self.speed
        self.shooter_rect.y = self.y




        