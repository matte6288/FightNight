
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
        numcols=0
        numrows=0
        size = 192
        if (self.name == "slash" or self.name == "thrust" or self.name == "punch"):
            numcols = 5
            numrows = 3
        if (self.name == "buff" or self.name == "debuff" or self.name == "shimmer" or self.name == "shield"):
            numcols = 5
            numrows = 6
        if (self.name == "cure"):
            numcols = 5
            numrows = 8
        if (self.name == "barrier or burst"):
            numcols = 5
            numrows = 10
        for i in range(numrows):
            for j in range(numcols):
                self.images.append(pygame.image.load("images/MoveSprites/"+name+"/"+name+str((i*numcols)+j+1)+".png"))