import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        print('UP       Button Pressed')
        ship.moving_up == True
    elif event.key == pygame.K_DOWN:
        print('DOWN     Button Pressed')
        ship.moving_down == True

def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit is not reached yet

    # Create new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        print('UP - released       Button  UN - Pressed')
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        print('Down - released       Button  UN - Pressed')
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''Start a new game if clicked'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        #reset game stats
        ai_settings.initialize_dynamic_settings()

        # reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #hide mouse curser
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #Empty Aliens and bullets:
        aliens.empty()
        bullets.empty()

        #Create a new fleet and centre the ship\
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings,screen, stats, sb, ship, alien, bullets, play_button):
    # Update images on screen and flip to new screen

    # Redraw the screen during each pass of the loop
    screen.fill(ai_settings.bg_colour)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Drawing the ship
    ship.blitme()

    # Drawing the alien
    alien.draw(screen)

    # Draw the score to the screen
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen display
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Update position of bullets and delete old bullets

    bullets.update()

    # Get rid of bullets that have dissappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet
        bullets.empty()
        # Speed up game
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

        # Increase level
        stats.level +=1
        sb.prep_level()

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):

    # Check for any bullets that have hit aliens
    # if that have hit, get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_scores(stats, sb)





def get_number_aliens_x(ai_settings, alien_width):
    ''' Determine the number of aliens that fit in a row'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determine the number of aliens that fit on the screen'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):

    '''Create an alien and place it in a row'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):

    '''Create a full fleet of aliens'''
    # create an alien and find the number of aliens in a row
    # Spacing between alien is equal to one width alien

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in its row
            create_alien(ai_settings,screen,aliens,alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''To respond if aliens have reached an edge'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''Drop the aliens down and change the direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''Respond to ship being hit by Alien'''
    # Decrement ships left
    if stats.ships_left > 0:

        stats.ships_left -= 1

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Update Scoreboard
        sb.prep_ships()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''Check if any aliens have hit the bottom of the screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Same as if a ship had been hit
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):

    '''check if aliens at edge'''
    check_fleet_edges(ai_settings, aliens)
    '''Update the positions of all aliens'''
    aliens.update()

    #Look for alien ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_high_scores(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()






