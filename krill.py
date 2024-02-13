"""
Author: Youssef Elsokkary
File: enemy.py
Date completed: 1/17/2024
Creates a Krill object that heals upon contact with the player.
"""

import unittest

import pygame
from game_object import GameObject
from CONSTANTS import GRID_SIZE

class Krill(GameObject):
    def __init__(self, x, y, player):
        """
        Initialize a Krill object.

        Args:
        - x: X-coordinate of the krill's position.
        - y: Y-coordinate of the krill's position.
        - player: Player object representing the main character.
        """
        super().__init__('k', x, y)  # 'k' represents krill
        self.image = pygame.transform.scale(pygame.image.load("assets/krill.jpg"), (GRID_SIZE, GRID_SIZE))
        self.player = player

    def apply_effect(self):
        """
        Apply the healing effect to the player when they come in contact with the krill.
        """
        # This method is called when the player goes over the 
        self.player.heal()
        print("Player healed!")

    def moveTo(self, x, y):
        """Move the Krill to a new position."""
        self.rect.x = x
        self.rect.y = y

"""
# Uncomment the following when you want to run the unittests

class TestKrill(unittest.TestCase):
    def setUp(self):
        self.player_mock = unittest.mock.Mock()
        self.krill = Krill(0, 0, self.player_mock)

    def test_initialization(self):
        self.assertEqual(self.krill.symbol, 'k')
        self.assertEqual(self.krill.rect.x, 0)
        self.assertEqual(self.krill.rect.y, 0)
        self.assertEqual(self.krill.image.get_size(), (GRID_SIZE, GRID_SIZE))
        self.assertEqual(self.krill.player, self.player_mock)

    @unittest.mock.patch('builtins.print')
    def test_apply_effect(self, mock_print):
        self.krill.apply_effect()
        self.player_mock.heal.assert_called_once()
        mock_print.assert_called_once_with("Player healed!")

if __name__ == '__main__':
    unittest.main()
"""
#The Krill class encapsulates its data (position, image, player) and behavior (apply_effect method) together.
#However, the attributes are not encapsulated with access modifiers.