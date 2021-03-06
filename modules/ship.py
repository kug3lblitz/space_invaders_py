import pygame

class Ship():
    def __init__(self, game_settings, screen):
        """initialize ship and set starting position"""
        self.screen = screen
        self.game_settings = game_settings

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store decimal value for ship's center
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        # check ship position and update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center ship on screen"""
        self.center = self.screen_rect.centerx
