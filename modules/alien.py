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
