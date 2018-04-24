import sys, pygame
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

def check_events(game_settings, screen, ship, bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
    bullets.update()

    # remove bullets that have passed offscreen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

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

def update_screen(game_settings, screen, ship, aliens, bullets):
    """update images on screen and flip to the new screen"""
    # redraw screen on each pass through the loop
    screen.fill(game_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # make the most recently drawn screen visible
    pygame.display.flip()
