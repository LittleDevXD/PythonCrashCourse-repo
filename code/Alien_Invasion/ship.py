import pygame

class Ship:
    def __init__(self, ai_game):
        # Screen rect
        self.game = ai_game.screen
        self.game_rect = self.game.get_rect()

        # Ship image and rect
        self.ship = pygame.image.load('images/player.png')
        self.ship_rect = self.ship.get_rect()

        # Position of the ship
        self.ship_rect.midbottom = self.game_rect.midbottom

        # Setting
        self.setting = ai_game.setting
        self.x = float(self.ship_rect.x)

        # Moving ship
        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.game.blit(self.ship, self.ship_rect)

    def update(self):
        if self.move_right and self.ship_rect.right < self.game_rect.right:
            self.x += self.setting.ship_speed
        elif self.move_left and self.ship_rect.left > 0:
            self.x -= self.setting.ship_speed

        self.ship_rect.x = self.x
