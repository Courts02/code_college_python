class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 850 
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        self.ship_limit = 3    
        self.ship_width = 90
        self.ship_height = 128

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        
        # Modify bomb settings for better visibility
        self.bomb_width = 20      # Diameter of the bomb
        self.bomb_height = 20     # Keep it same as width for circular shape
        self.bomb_color = (255, 0, 0)  # Keep bright red
        self.bomb_speed = 3.0     # Slower than bullets
        self.bombs_allowed = 3   
        self.bomb_recharge_time = 10000  # 3 seconds in milliseconds
        self.bomb_explosion_radius = 200  # Radius of explosion effect

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3
        self.bullet_speed = 3
        self.alien_speed = 1.5
        self.bomb_speed = 2.0  # Initial bomb speed

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bomb_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self, difficulty):
        """Adjust game settings based on difficulty level."""
        if difficulty == 'Easy':
            self.alien_speed = 1.0
            self.bullets_allowed = 6
            self.bomb_recharge_time = 5000  # 5 seconds
            self.fleet_drop_speed = 5
            self.alien_points = 25
        elif difficulty == 'Medium':
            self.alien_speed = 1.5
            self.bullets_allowed = 4
            self.bomb_recharge_time = 10000  # 10 seconds
            self.fleet_drop_speed = 10
            self.alien_points = 50
        elif difficulty == 'Hard':
            self.alien_speed = 2.0
            self.bullets_allowed = 3
            self.bomb_recharge_time = 15000  # 15 seconds
            self.fleet_drop_speed = 15
            self.alien_points = 100