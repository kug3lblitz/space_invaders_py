class Settings():
    """A class housing all settings for Alien Invasion"""

    def __init__(self):
        """initialize the settings module"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (48, 51, 49)

        #ship settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
