import sys
import pygame

def check_events():
    '''respond to key presses'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, player):

    screen.fill(settings.bg_color)
    player.blitme()

    # Make the most recent drawn screen visisble
    pygame.display.flip()

def check_keydown_events(event, settings, screen, player):
#
    # Respond to keypresses

    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    # elif event.key == pygame.K_SPACE:
    #     fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        print('UP       Button Pressed')
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        print('DOWN     Button Pressed')
        player.moving_down = True

def check_keyup_events(event,player):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
        # print(player.center)
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        print('UP - released')
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        print('Down - released ')
        player.moving_down = False

def check_events(settings, screen, player):
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

