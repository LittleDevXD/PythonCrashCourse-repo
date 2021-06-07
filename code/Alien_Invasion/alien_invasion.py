import pygame
import sys
import random
from setting import Setting
from ship import Ship
from bullet import Bullet
from aliens import Alien
from star import Star

class AlienInvasion:
    """ALL OF THE GAME FUNCTIONS IN HERE"""

    def __init__(self):
        """Initialize pygame and create materials."""
        pygame.init()
        self.setting = Setting()

        # Screen
        self.screen = pygame.display.set_mode(
                      (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.bg_color = self.setting.bg_color

        # Creating ship instance
        self.ship = Ship(self)

        # Bullet group
        self.bullets = pygame.sprite.Group()

        # Alien group
        self.aliens = pygame.sprite.Group()

        # Star group
        self.stars = pygame.sprite.Group()

        # Adding alien to alien group
        self._create_fleet()

        # Adding star to star group
        self._create_stars()

    def run_game(self):
        """Game Loop"""
        while True:
            self._check_events()
            # Update the positions 
            self.ship.update()
            self.bullets.update()
            self._update_aliens()
            # Remove old bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)
            self._update_screen()

    def _check_events(self):
        """ Check the input from user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_presses(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_presses(event)

    def _update_screen(self):
        """ Add resources to screen """
        self.screen.fill(self.bg_color)
        # Draw Stars
        self.stars.draw(self.screen)

        # Draw ship
        self.ship.blitme()
        
        # Draw bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draw Aliens
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown_presses(self, event):
        """All keydown presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
    
    def _check_keyup_presses(self, event):
        """All keyup presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _fire_bullets(self):
        # Adding new bullets to bullets Group
        if len(self.bullets) < self.setting.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # Calculation for each row
        alien = Alien(self)
        alien_width = alien.rect.width - 10
        screen_width = self.setting.screen_width
        available_space_x = screen_width - (2 * alien_width)
        alien_number_x = available_space_x // (2 * alien_width)

        # Calculation for numbers of rows
        alien_height = alien.rect.height - 10
        screen_height = self.setting.screen_height
        ship_height = self.ship.ship_rect.height
        available_space_y = screen_height - (2 * alien_height) - ship_height
        row_numbers =  available_space_y // (2 * alien_height) 

        # First loop for each row
        for row_number in range(row_numbers):
            # Second loop for individual alien
            for alien_x in range(alien_number_x):
                self._create_alien(row_number, alien_x)

    def _create_alien(self, row_number, alien_x):
        """ Create individual alien and its position """
        alien = Alien(self)
        alien_width = alien.rect.width - 10
        alien_height = alien.rect.height - 10
        alien.rect.x = alien_width + 2 * alien_width * alien_x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _create_stars(self):
        star = Star()
        star_numbers = 10
        for star_number in range(star_numbers):
            star = Star()
            star.rect.x = random.randint(0, 1000)
            star.rect.y = random.randint(0, 600)
            self.stars.add(star)

    def _update_aliens(self):
        self.aliens.update()

        
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()