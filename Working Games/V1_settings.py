

class Settings():

    # A class to store all the settings for the game

    def __init__(self):
        '''Initialize the game's settings.'''

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 20, 200)

        # Ship Setting
        self.player_speed_factor = 10

        # cannon settings
        self.cannon_speed_factor = 10

        self.cannon_width = 10

        self.cannon_height = 5
        self.cannon_colour = 0, 0, 0
        self.cannon_allowed = 1000