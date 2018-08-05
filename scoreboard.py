''' A class to report scoring information'''
import pygame.ftfont

class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        '''initialise scorekeeping attributes'''

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for storing information
        self.text_colour = (30, 30, 30)
        self.font = pygame.ftfont.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        #Turn the score into a rendered image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.ai_settings.bg_colour)

        # Display the score in the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # Draw the score on the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        # Turn high score into a rendered image
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour, self.ai_settings.bg_colour)

        # Center the high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
