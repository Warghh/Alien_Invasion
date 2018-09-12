import pygame
from pygame.sprite import Sprite

class cannon(Sprite):
    # A class to manage the cannons


    def __init__(self, settings, screen, player):
        # Create bullet object at the ships current position
        super(cannon, self).__init__()
        self.screen = screen

        # Create a bullet rect at ships current position
        self.rect = pygame.Rect(0,0,settings.cannon_width, settings.cannon_height)
        self.rect.centerx = player.rect.centerx
        self.rect.midright = player.rect.midright

        # Store the bullets position as a decimal
        self.x = float(self.rect.x)

        self.colour = settings.cannon_colour
        self.speed_factor = settings.cannon_speed_factor

    def update(self):
        #Move the bullet up the screen
        self.x +=self.speed_factor
        #Update the rect position
        self.rect.x = self.x


    def draw_cannon(self):
        # Draw the bullet on the screen
        pygame.draw.rect(self.screen, self.colour, self.rect)