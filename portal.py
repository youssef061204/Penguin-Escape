"""
Author: Youssef Elsokkary
File: enemy.py
Date completed: 1/17/2024
Creates a Portal that allows you to teleport to another Portal.
"""

import unittest
from game_object import GameObject
import pygame
from unittest.mock import Mock

class Portal(GameObject):
    def __init__(self, x, y, destination_x, destination_y):
        """
        Initialize a Portal object.

        Args:
        - x: X-coordinate of the portal's position.
        - y: Y-coordinate of the portal's position.
        - destination_x: X-coordinate where the player will be teleported.
        - destination_y: Y-coordinate where the player will be teleported.
        """
        super().__init__('p', x, y)
        self.destination_x = destination_x
        self.destination_y = destination_y

    def teleport(self, player):
        """
        Teleport the player to the destination coordinates.

        Args:
        - player: Player object representing the main character.
        """
        player.rect.x = self.destination_x
        player.rect.y = self.destination_y
        print(f"Player teleported to ({self.destination_x}, {self.destination_y})")

"""
# Uncomment the following when you want to run the unittests
class TestPortal(unittest.TestCase):
    def setUp(self):
        self.player_mock = Mock()
        self.portal = Portal(0, 0, 100, 100)

    def test_initialization(self):
        self.assertEqual(self.portal.symbol, 'p')
        self.assertEqual(self.portal.rect.x, 0)
        self.assertEqual(self.portal.rect.y, 0)
        self.assertEqual(self.portal.destination_x, 100)
        self.assertEqual(self.portal.destination_y, 100)

    def test_teleport(self):
        self.portal.teleport(self.player_mock)
        self.assertEqual(self.player_mock.rect.x, 100)
        self.assertEqual(self.player_mock.rect.y, 100)
        print.assert_called_once_with("Player teleported to (100, 100)")

if __name__ == '__main__':
    unittest.main()
"""
#The Portal class encapsulates its data (position, destination) and behavior (teleport method) together.
#Like the others, the attributes are not encapsulated with access modifiers.