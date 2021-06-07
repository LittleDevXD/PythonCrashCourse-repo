class Setting:
    """This class includes all game settings"""
    def __init__(self):
        # Width and height of game window
        self.screen_height = 600
        self.screen_width = 1000
        # Background color
        self.bg_color = (200, 200, 200) 

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1