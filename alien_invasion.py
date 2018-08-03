import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button




def run_game():


    # Initialise game window and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make play button
    play_button = Button(ai_settings, screen, 'Play')

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)


    # Make a ship
    ship = Ship(ai_settings, screen)


    # Make a group to store bullets in
    bullets = Group()

    # Making a fleet of aliens
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make an alien for the game
    alien = Alien(ai_settings, screen)

    # Start the main loop for the game
    while True:

            # Watch for keyboard and mouse events
            gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

            if stats.game_active:

                # Moving the ship
                ship.update()

                # Update Bullets
                gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

                # Update the aliens
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            # Update the screen
            gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)






run_game()
