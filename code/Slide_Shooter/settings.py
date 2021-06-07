class Setting:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (80, 80, 230)

        # Shooter settings
        self.shooter_speed = 1.5

        # Bullet settings
        self.beam_speed = 1.0
        self.beam_width = 15
        self.beam_height = 3
        self.beam_color = (60, 60, 60)
        self.beam_allowed = 5