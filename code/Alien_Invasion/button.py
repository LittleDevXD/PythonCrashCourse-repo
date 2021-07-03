import pygame.font
import pygame

class Button:
    def __init__(self, ai_game, msg):
        # Get the screen rect
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Button
        self.bg_color = (0, 255, 0)
        self.color = (255, 255, 255)
        self.height, self.width = 50, 200
        self.font = pygame.font.SysFont(None, 48)

        # Button rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Render the message and disply on button"""
        self.msg_image = self.font.render(msg, True, self.color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)