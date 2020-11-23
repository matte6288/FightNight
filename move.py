
import pygame

class move:

    """Represents a move."""

    def __init__(self, name):
        """Initialize attributes to represent a move."""
        self.images= []
        self.name = name
        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0
        self._loadImages(name)

    def _loadImages(self, name):
        size=0
        if (self.name == "slash" or self.name == "thrust" or self.name == "punch"):
            size=15
        if (self.name == "buff" or self.name == "debuff" or self.name == "shimmer" or self.name == "shield" or self.name == "jim"):
            size=30
        if (self.name == "heal"):
            size=40
        if (self.name == "barrier" or self.name == "burst"):
            size=50
        print(3)
        for i in range(size):
            self.images.append(pygame.image.load("images/MoveSprites/"+name+"/"+name+str(i+1)+".png"))

