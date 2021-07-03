import pygame
from setting import Setting

class GameStats:
    def __init__(self):
        self.settings = Setting()
        # If the ships_left is zero the game stops
        self.game_active = False
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.level = 1
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_left
        self.score = 0