"""
Author: Youssef Elsokkary
File: game_object.py
Date completed: 1/17/2024
Defines the GameObject class, used as a parent class for all other objects
"""
import unittest
import pygame
from CONSTANTS import GRID_SIZE

class GameObject(pygame.sprite.Sprite):
    def __init__(self, symbol, x, y):
        """
        Initialize a GameObject.

        Args:
        - symbol: A symbol representing the type of the game object.
        - x: X-coordinate of the game object's position.
        - y: Y-coordinate of the game object's position.
        """
        super().__init__()
        self.symbol = symbol  # A symbol representing the type of the game object
        self.rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)

    def update_position(self, x, y):
        """
        Update the position of the game object.

        Args:
        - x: New X-coordinate of the game object's position.
        - y: New Y-coordinate of the game object's position.
        """
        self.rect.x = x
        self.rect.y = y

"""
# Uncomment the following when you want to run the unittests
class TestGameObject(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject('g', 0, 0)

    def test_initialization(self):
        self.assertEqual(self.game_object.symbol, 'g')
        self.assertEqual(self.game_object.rect.x, 0)
        self.assertEqual(self.game_object.rect.y, 0)
        self.assertEqual(self.game_object.rect.width, GRID_SIZE)
        self.assertEqual(self.game_object.rect.height, GRID_SIZE)

    def test_update_position(self):
        self.game_object.update_position(10, 20)
        self.assertEqual(self.game_object.rect.x, 10)
        self.assertEqual(self.game_object.rect.y, 20)

if __name__ == '__main__':
    unittest.main()
"""

#The GameObject class encapsulates its data (symbol, position) and behavior (update_position method) together.
#The attributes are not encapsulated with access modifiers.