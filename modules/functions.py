import sys, pygame

def check_events(ship):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(game_settings, screen, ship):
    """update images on screen and flip to the new screen"""
    # redraw screen on each pass through the loop
    screen.fill(game_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen visible
    pygame.display.flip()
