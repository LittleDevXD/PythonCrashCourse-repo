import pygame
import sys
import random
from setting import Setting
from ship import Ship
from bullet import Bullet
from aliens import Alien
from star import Star
from game_stats import GameStats
from time import sleep
from button import Button
from score_board import Scoreboard

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

        # Game-Stats instance
        # create a score board
        self.game_stats = GameStats()
        self.sb = Scoreboard(self)

        # Adding alien to alien group
        self._create_fleet()

        # Adding star to star group
        self._create_stars()

        # Play Button
        self.button = Button(self, "Play")

    def run_game(self):
        """Game Loop"""
        while True:
            self._check_events()
            
            # Check if any ships left
            if self.game_stats.game_active:
                # Update the positions 
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_button(self, mouse_pos):
        """Start a new game if the player presses play button"""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_stats.game_active:
            self._reset_game()
    
    def _reset_game(self):
        # Hide mouse cursor
        pygame.mouse.set_visible(False)

        self.game_stats.reset_stats()
        self.game_stats.game_active = True

        # Empty aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Restore setting
        self.setting.initialized_dynamic_setting()

        self.sb.prep_score()
        self.sb.prep_high_score()
        self.sb.prep_level()

        self.sb.prep_ships()

    def _update_screen(self):
        """ Add resources to screen """
        self.screen.fill(self.bg_color)
        # Draw Stars
        self.stars.draw(self.screen)

        # Draw ship
        self.ship.blitme()

        # Display score
        self.sb.show_score()
        
        # Draw bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draw Aliens
        self.aliens.draw(self.screen)

        # Draw Button
        if not self.game_stats.game_active:
            self.button.draw_button()

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
        elif event.key == pygame.K_p and not self.game_stats.game_active:
            self._reset_game()
    
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

    def _update_bullets(self):
        # Update the bullet position
        self.bullets.update()

        # Remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self._detect_bullets_aliens_collisions()

    def _detect_bullets_aliens_collisions(self):
        # Check collision and delete aliens from sprite
        collision = pygame.sprite.groupcollide(self.bullets, 
                                    self.aliens, True, True)

        # Create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()
            self.game_stats.level += 1
            self.sb.prep_level()

        if collision:
            for aliens in collision.values():
                self.game_stats.score += self.setting.aliens_point * len(aliens)
            self.sb.check_high_score()
            self.sb.prep_score()

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
        ship_height = self.ship.rect.height
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
        """ Update Aliens' Positions """
        self.aliens.update()
        self._check_fleet_edges()

        # Alien-Ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._alien_reaches_bottom()

    def _alien_reaches_bottom(self):
        """CHECK IF ANY ALIEN TOUCHES THE BOTTOM OF THE SCREEN"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        # Reduce amount of ships left
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self.sb.prep_ships()

            # Empty bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Recreate
            self._create_fleet()
            self.ship.center_ship()

            # Wait 
            sleep(0.5)
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()