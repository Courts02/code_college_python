import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Get display info for fullscreen
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode(
            (info.current_w, info.current_h), pygame.FULLSCREEN
        )
        
        pygame.display.set_caption("Alien Invasion")

        # Store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.settings.screen_width = info.current_w
        self.settings.screen_height = info.current_h

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an active state
        self.stats.game_active = True
        # Start Alien Invasion in an inactive state
        self.stats.game_active = False

        # draw the play button if the game is inactive
        self.play_button = Button(self, "Play")

        pygame.mixer.init()  # Initialize sound mixer

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Load sound effects
        self.bullet_sound = pygame.mixer.Sound("sounds/space-slash-236689.mp3")
        self.bullet_sound.set_volume(0.5)  # Adjust volume (0.0 - 1.0)
        # self.ship_sound = pygame.mixer.Sound("space-animal-104986.mp3")
        self.game_over_sound = pygame.mixer.Sound("sounds/game-over-arcade-6435.mp3")
        # self.bomb_explosion_sound = pygame.mixer.Sound("large-underwater-explosion-190270.mp3")  # Use your actual file
        # self.bomb_explosion_sound.set_volume(0.5)  # Adjust volume if needed
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion-under-snow-sfx-230505.mp3") 
        self.explosion_sound.set_volume(0.5)  # Adjust volume if needed


        # Load and play background music (loop indefinitely)
        pygame.mixer.music.load("sounds/ambient-soundscapes-007-space-atmosphere-304974.mp3")
        pygame.mixer.music.set_volume(0.2)  # Adjust volume (0.0 - 1.0)
        pygame.mixer.music.play(-1)  # Loop forever

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()

                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)  # Limit FPS to 60

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  # Quit the game
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.game_active = True
            pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""      
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullet_sound.play()
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and remove old ones."""
        self.bullets.update()

        # Remove bullets that have gone off-screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            self.explosion_sound.play()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.check_high_score()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        self.settings.fleet_direction = -1
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Determine available space for aliens
        available_x_space = self.settings.screen_width - (2 * alien_width)
        available_y_space = self.settings.screen_height - (3 * alien_height)

        # Calculate number of aliens per row and columns
        number_aliens_x = available_x_space // (2 * alien_width)
        number_rows = available_y_space // (2 * alien_height)

        # Create the fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number * 2 * alien_width, row_number * 2 * alien_height)

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet and check for collisions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_width or alien.rect.left <= 0:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            self.sb.prep_ships()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.game_over_sound.play

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            self.sb.prep_level()
            self.sb.prep_ships()
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False) 

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)          
        pygame.draw.rect(self.screen, (255, 0, 0), self.play_button.rect, 2)  # Red border

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
