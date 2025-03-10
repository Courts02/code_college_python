import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bomb(Sprite):
    """A class to manage bombs dropped by the ship."""
    def __init__(self, ai_game):
        """Initialize the bomb."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bomb_color

        # Create a bomb rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width,
            self.settings.bomb_height)
        self.rect.midbottom = ai_game.ship.rect.midbottom  # Changed from midtop to midbottom
        
        # Store the bomb's position as a float
        self.y = float(self.rect.y)

        # Explosion attributes
        self.is_exploding = False
        self.explosion_start = 0
        self.explosion_duration = 1000  # Duration in milliseconds
        self.explosion_radius = self.settings.bomb_explosion_radius

    def start_explosion(self):
        """Start the explosion animation."""
        if not self.is_exploding:
            self.is_exploding = True
            self.explosion_start = pygame.time.get_ticks()
            print(f"Explosion started at ({self.rect.centerx}, {self.rect.centery})")

    def update(self):
        """Move the bomb down the screen."""
        if not self.is_exploding:
            self.y -= self.settings.bomb_speed  # Changed from -= to += to move downward
            self.rect.y = self.y

    def _update_bombs(self):
        """Update position of bombs and check for collisions."""
        self.bombs.update()

        # Check for bomb-alien collisions
        self._check_bomb_alien_collisions()

        # Remove bombs that have gone off screen
        for bomb in self.bombs.copy():
            if bomb.rect.top >= self.settings.screen_height:
                self.bombs.remove(bomb)
                self.bomb_explosion_sound.play()

    def draw_bomb(self):
        """Draw the bomb and its explosion if active."""
        if self.is_exploding:
            # Calculate explosion animation progress
            current_time = pygame.time.get_ticks()
            progress = (current_time - self.explosion_start) / self.explosion_duration
            
            if progress <= 1.0:
                # Create a surface for the explosion
                explosion_surface = pygame.Surface((self.explosion_radius * 2, 
                                                 self.explosion_radius * 2), pygame.SRCALPHA)
                
                # Calculate alpha value (fade out)
                alpha = int((1 - progress) * 255)
                
                # Draw the explosion circle
                pygame.draw.circle(explosion_surface, (*self.settings.bomb_color, alpha),
                                 (self.explosion_radius, self.explosion_radius),
                                 self.explosion_radius)
                
                # Draw the explosion centered on the bomb
                explosion_rect = explosion_surface.get_rect()
                explosion_rect.center = self.rect.center
                self.screen.blit(explosion_surface, explosion_rect)
        else:
            # Draw the normal bomb
            pygame.draw.circle(self.screen, self.color, self.rect.center, 
                             self.settings.bomb_width // 2)