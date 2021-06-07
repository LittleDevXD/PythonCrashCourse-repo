import pygame
import sys
from settings import Setting
from shooter import Shooter
from beams import Beam

class SlideShooter:
    def __init__(self):
        # Setting instance 
        self.setting = Setting()

        # Screen
        self.screen = pygame.display.set_mode(
                        (self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption('Slide Shooter')

        # Bullets Group
        self.beams = pygame.sprite.Group()

        # Shooter instance
        self.shooter = Shooter(self)

    def run_game(self):
        """ Main Game Loop """
        while True:
            self._check_events()
            self.shooter.update()
            self.beams.update()
            # Remove old bullets
            for beam in self.beams:
                if beam.beam_rect.right < 0:
                    self.beams.remove(beam)
            self._update_screen()
            
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.shooter.blitme()
        # Draw bullets
        for beam in self.beams.sprites():
            beam.draw_bullet()
        pygame.display.flip()

    def _check_events(self):
        """ Check all events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Check Keydown events """
        if event.key == pygame.K_UP:
            self.shooter.move_up = True
        elif event.key == pygame.K_DOWN:
            self.shooter.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """ Check Keyup events """
        if event.key == pygame.K_UP:
            self.shooter.move_up = False
        elif event.key == pygame.K_DOWN:
            self.shooter.move_down = False

    def _fire_bullets(self):
        """ Add new bullets to group """
        if len(self.beams) < self.setting.beam_allowed:
            new_bullet = Beam(self)
            self.beams.add(new_bullet)

if __name__ == '__main__':
    game = SlideShooter()
    game.run_game()