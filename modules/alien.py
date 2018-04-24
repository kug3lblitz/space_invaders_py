import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, game_settings, screen):
        """initialize the alien and set starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien to the right or left"""
        self.x += (self.game_settings.alien_speed_factor *
                    self.game_settings.fleet_direction)
        self.rect.x = self.x
