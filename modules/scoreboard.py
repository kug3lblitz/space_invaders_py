import pygame.font

class Scoreboard():
    """class to report scoring information"""

    def __init__(self, game_settings, screen, stats):
        """initialize scorekeeping attrs"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # font setting for scoring info
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial score image
        self.prep_score()

    def prep_score(self):
        """turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                self.game_settings.bg_color)

        # display score in top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
