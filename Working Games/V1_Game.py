import sys
import pygame

from V1_settings import Settings
from V1_player import Player
import V1_game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Game V1")

    player = Player(settings, screen)



    # Start main loop for game
    while True:

        gf.check_events(settings, screen, player)

        player.update()

        gf.update_screen(settings, screen, player)

run_game()

