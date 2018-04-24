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

# how many aliens fit across and down the screen
# available_space_x = ai_settings.screen_width – (2 * alien_width)
# number_aliens_x = available_space_x / (2 * alien_width)

def create_fleet(game_settings, screen, aliens):
    """create a full fleet of aliens"""
    # create alien and find the number of aliens in a row
    # spacing between each alien is one alien width
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    avaliable_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))

    #create the first row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

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
