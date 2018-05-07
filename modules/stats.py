class GameStats():
    """tracks statistics for invasion game"""

    def __init__(self, game_settings):
        """initialize statistics"""
        self.game_settings = game_settings
        self.reset_stats()
        # because high score should not be reset,
        # we initialize it here instead of reset_stats
        self.high_score = 0

        # start game in active state
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
