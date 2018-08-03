class Settings():
    '''A class to store all the settings for Alien Invasion'''


    def __init__(self):
        '''Initialise the game's settings'''
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_colour = (230, 230, 230)


        # Bullet settings
        self.bullet_speed_factor = 100
        self.bullet_width = 200
        self.bullet_height = 30
        self.bullet_colour = 50,60,60
        self.bullets_allowed = 100

        #Ship Setting
        self.ship_speed_factor = 20
        self.ship_limit = 3

        #Alien settings
        self.alien_speed_factor = 8
        self.fleet_drop_speed = 20
        #fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speed_up_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialise dynamic game settings for settings that will change during the game'''
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 50
        self.alien_speed_factor = 5

        self.fleet_direction = 1

    def increase_speed(self):
        '''Increase speed settings'''
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale



