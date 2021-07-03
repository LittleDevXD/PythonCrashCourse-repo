import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # Screen rect
        self.game = ai_game.screen
        self.game_rect = self.game.get_rect()

        # Ship image and rect
        self.ship = pygame.image.load('images/player.png')
        self.image = pygame.image.load('images/player.png')
        self.rect = self.ship.get_rect()

        # Position of the ship
        self.rect.midbottom = self.game_rect.midbottom

        # Setting
        self.setting = ai_game.setting
        self.x = float(self.rect.x)

        # Moving ship
        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.game.blit(self.ship, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.game_rect.right:
            self.x += self.setting.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.game_rect.midbottom
