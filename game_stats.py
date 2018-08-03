'''Game statistics to keep track of the score'''

class GameStats():

    def __init__(self, ai_settings):
        '''Initiaise Statistics'''
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start invasion in Inactive state
        self.game_active = False

    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

