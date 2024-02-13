
"""
Author: Daniel Chen
File: button.py
Date completed: 01/16/2023
Creates a pressable button object.
"""
from game_object import GameObject


class Button(GameObject):
    """Creates a pressable button object."""

    def __init__(self, x, y):
        """
        Create the button.
        
        Args:
            x (int): x-coordinate of the button.
            y (int): y-coordinate of the button.
        """
        super().__init__("u", x, y)
        self.rect.x = x
        self.rect.y = y

    def activate(self, level):
        """Activate the button"""
        level.resetLava()


class DestroyableButton(Button):
    """Creates a destroyable button object."""
    
    def __init__(self, x, y):
        """
        Create the button.

        Args:
            x (int): x-coordinate of the button.
            y (int): y-coordinate of the button.
        """
        super().__init__(x, y)
        self.rect.x = x
        self.rect.y = y

    def activate(self, level):
        """Activate the button"""
        super().activate(level)
        level.changeSquare(self.rect.x, self.rect.y, "b")
