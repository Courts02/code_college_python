import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should be loaded from file
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score from a JSON file."""
        filename = 'high_scores.json'
        try:
            with open(filename) as f:
                data = json.load(f)
                return data['high_score']
        except FileNotFoundError:
            # If file doesn't exist, create it with default high score
            self.save_high_score(0)
            return 0

    def save_high_score(self, score):
        """Save the high score to a JSON file."""
        filename = 'high_scores.json'
        with open(filename, 'w') as f:
            json.dump({'high_score': score}, f)