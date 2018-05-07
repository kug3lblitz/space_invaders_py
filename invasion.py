import pygame
from pygame.sprite import Group
from modules.settings import Settings
from modules.stats import GameStats
from modules.scoreboard import Scoreboard
from modules.button import Button
from modules.ship import Ship
from modules.alien import Alien
import modules.functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Invaders!!")

    #create play button
    play_button = Button(game_settings, screen, "Play")

    # create an instance to store game statistics and create scoreboard
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    # create player ship, a group of bullets, a group of aliens
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # create alien fleet
    gf.create_fleet(game_settings, screen, ship, aliens)

    # main loop
    while True:
        gf.check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
