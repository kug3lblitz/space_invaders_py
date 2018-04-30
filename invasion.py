import pygame
from pygame.sprite import Group
from modules.settings import Settings
from modules.ship import Ship
from modules.alien import Alien
import modules.functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Invaders!!")

    # create player ship, a group of bullets, a group of aliens
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # create alien fleet
    gf.create_fleet(game_settings, screen, ship, aliens)

    # main loop
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(game_settings, aliens)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

run_game()
