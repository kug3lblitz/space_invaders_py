class Settings():
    """A class housing all settings for Alien Invasion"""

    def __init__(self):
        """initialize the settings module"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 31, 30)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10

        # rate at which game speeds up
        self.speedup_scale = 1.1

        # rate of point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that will change throughout"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet direction of 1 represents right, -1 left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
