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
        self.ship_left = 3

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Speeding up the game
        self.speed_up_scale = 1.1

        self.initialized_dynamic_setting()

    def initialized_dynamic_setting(self):
        """Restore the initial settings"""
        self.alien_speed = 1
        self.ship_speed = 1.5
        self.ship_speed = 1.0

        self.fleet_direction = 1

        self.aliens_point = 50

    def increase_speed(self):
        """Increase Speed By 1.1"""
        self.alien_speed *= self.speed_up_scale
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale

