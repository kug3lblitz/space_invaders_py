import pygame
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

    # main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings, screen, ship)

run_game()
