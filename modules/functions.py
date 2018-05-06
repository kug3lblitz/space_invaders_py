import sys, pygame
from time import sleep
from modules.bullet import Bullet
from modules.alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(game_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet"""
    #create new bullet and add to bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, stats, play_button, ship, aliens, bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """start new game when player clicks play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        game_settings.initialize_dynamic_settings()
        start_game(game_settings, screen, stats, play_button, ship, aliens, bullets, check_play_button)

def start_game(game_settings, screen, stats, play_button, ship, aliens, bullets, check_play_button):
        #hide the mouse cursor
        pygame.mouse.set_visible(False)

        # reset game stats
        stats.reset_stats()
        stats.game_active = True

        # empty aliens, bullets lists
        aliens.empty()
        bullets.empty()

        # create new fleet, center ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """update position of bullets and get rid of old bullets"""
    bullets.update()

    # remove bullets that have passed offscreen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)

def check_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):
    """respond to bullet-alien collisions"""
    # check if any bullets have hit aliens, and remove both if true
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        stats.score += game_settings.alien_points
        sb.prep_score()

    if len(aliens) == 0:
        # destroy existing bullets, increase speed, and create new fleet
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

def get_number_aliens_x(game_settings, alien_width):
    """determine the number of aliens that will fit in a row"""
    avaliable_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

# available space y = game_settings.screen_height - 3 * alien_height - ship_height
# number of rows = available height y / (2 * alien height)

def get_number_rows(game_settings, ship_height, alien_height):
    """determine the number of rows of aliens that fit on screen"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it into the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

# how many aliens fit across and down the screen
# available_space_x = ai_settings.screen_width – (2 * alien_width)
# number_aliens_x = available_space_x / (2 * alien_width)

def create_fleet(game_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    # create alien and find the number of aliens in a row
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(game_settings, aliens):
    """respond if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    """drop the entire fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    """respond to ship being hit by alien"""
    if stats.ships_left > 0:
        # decrement ships remaining
        stats.ships_left -= 1

        # empty list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new alien fleet and center ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
    """check if any alien has reached bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treated as though ship has been hit
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    """check edges, update position of all aliens in the fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

    #look for aliens hitting bottom of screen
    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)

    #respond to alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("SHIP HIT! YOU DIED!")
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)

def update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """update images on screen and flip to the new screen"""
    # redraw screen on each pass through the loop
    screen.fill(game_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # draw score information
    sb.show_score()

    # draw play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # make the most recently drawn screen visible
    pygame.display.flip()
