

class Settings():

    # A class to store all the settings for the game

    def __init__(self):
        '''Initialize the game's settings.'''

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Setting
        self.player_speed_factor = 20