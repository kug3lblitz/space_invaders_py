import pygame
from pygame.sprite import Group
from modules.settings import Settings
from modules.ship import Ship
import modules.functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Xenophobia!!")

    # create player ship
    ship = Ship(game_settings, screen)
    # make a group to store bullets in
    bullets = Group()

    # main loop
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # remove bullets that have passed offscreen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

        gf.update_screen(game_settings, screen, ship, bullets)

run_game()
