import sys
import pygame
from cannon import cannon

def check_events():
    '''respond to key presses'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, player, cannons):

    screen.fill(settings.bg_color)
    player.blitme()

    # Redraw all bullets behind ship and aliens
    for cannon in cannons.sprites():
        cannon.draw_cannon()

    # Make the most recent drawn screen visisble
    pygame.display.flip()



def check_keydown_events(event, settings, screen, player, cannons):
#
    # Respond to keypresses

    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_cannon(settings, screen, player, cannons)

    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True

def check_keyup_events(event,player):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        # print(player.center)
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False

def check_events(settings, screen, player, cannons):
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, player, cannons)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def fire_cannon(settings, screen, player, cannons):
    # Fire a bullet if limit is not reached yet

    # Create new bullet and add it to the bullets group
    if len(cannons) < settings.cannon_allowed:
        new_cannon = cannon(settings, screen, player)
        cannons.add(new_cannon)

def update_cannons(settings, screen, player, cannons):
    # Update position of bullets and delete old bullets

    cannons.update()

    # Get rid of bullets that have dissappeared
    for cannon in cannons.copy():
        if cannon.rect.bottom <= 0:
            cannons.remove(cannon)
    print(len(cannons))


