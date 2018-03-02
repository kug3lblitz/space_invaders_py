import sys, pygame
from modules.settings import Settings
from modules.ship import Ship

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
            (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Xenophobia!!")

    # create player ship
    ship = Ship(screen)

    # main loop
    while True:
        # watch for input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw screen on each pass through the loop
        screen.fill(game_settings.bg_color)
        ship.blitme()

        # make most recently drawn screen visible
        pygame.display.flip()

run_game()
