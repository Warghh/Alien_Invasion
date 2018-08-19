'''Class for a clickable button'''


import pygame.ftfont


class Button():
    '''Initialise screen attributes'''

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self. height = 20, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 50)

        # Build the buttons rect object and center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message only needs to be preppeed once
        self.prep_msg(msg)

    def prep_msg(self, msg):

        # Turn msg into rendered image and center text on button
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw a blank button and then draw the message
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


