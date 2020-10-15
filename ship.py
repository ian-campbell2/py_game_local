import pygame

class Ship:
    """A class to manage the ship."""

    def __init___(self, ai_game):
        """Initalize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get.rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating the ship's position based on movement flags."""
        #Update the ships x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1
        #update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    