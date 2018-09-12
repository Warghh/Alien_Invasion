import pygame

from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self, settings, screen):
        '''Initialise the ship and its starting position'''

        super(Player, self).__init__()

        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/Ship_2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ships center
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Update the ships movement based on the movement flag

        # edited - Update the ships center value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.settings.player_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.settings.player_speed_factor
        if self.moving_up and self.rect.top > 20:
            self.center_y -= self.settings.player_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.player_speed_factor

        # Update Rect object from self.center
        self.rect.centerx = self.center_x
        # Update Rect object from self.center
        self.rect.centery = self.center_y