import sys
import pygame

from V1_settings import Settings
from V1_player import Player
import V1_game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Game V1")

    player = Player(settings, screen)

    # Make a group to store bullets in
    cannons = Group()



    # Start main loop for game
    while True:

        gf.check_events(settings, screen, player, cannons)

        player.update()

        # Update Bullets
        gf.update_cannons(settings, screen, player, cannons)

        gf.update_screen(settings, screen, player, cannons)

run_game()

