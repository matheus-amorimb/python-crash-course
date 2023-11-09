import time
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            size=(self.settings.screen_width, self.settings.screen_height)
        )

        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption(title='Alien Invasion')

        self.ship = Ship(self)

        # Set the backgground image.
        self.bg = pygame.image.load(self.settings.background_image)

    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # The frame rate for the fame. Pygame will make the loop run exaclty 60 times per second.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.blitme()

        # Update the full display Surface to the screen
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
