"""
Author: Youssef Elsokkary
File: freeze.py
Date completed: 1/17/2024
Creates a freeze object that freezes the player for a specified time limit.
"""

import unittest
from unittest.mock import Mock
import pygame
import time
from game_object import GameObject
from CONSTANTS import GRID_SIZE


class Freeze(GameObject):
    def __init__(self, x, y, duration=2):
        """
        Initialize a Freeze object.

        Parameters:
        - x (int): The x-coordinate of the Freeze object.
        - y (int): The y-coordinate of the Freeze object.
        - duration (int): The duration (in seconds) for which the player will be frozen.
        """
        super().__init__('f', x, y)
        self.duration = duration
        self.is_frozen = False
        self.freeze_start_time = 0

    def freeze_player(self, player):
        """
        Freeze the player if they are not already frozen.

        Parameters:
        - player (Player): The player object to be frozen.
        """
        if not self.is_frozen:
            print("Player frozen!")
            self.is_frozen = True
            self.freeze_start_time = time.time()

    def update(self):
        """
        Update the freeze status, checking if the freeze duration has elapsed.
        """
        if self.is_frozen:
            current_time = time.time()
            elapsed_time = current_time - self.freeze_start_time

            if elapsed_time >= self.duration:
                print("Player unfrozen!")
                self.is_frozen = False

"""
# Uncomment the following when you want to run the unittests
class TestFreeze(unittest.TestCase):
    def setUp(self):
        self.player_mock = Mock()
        self.freeze = Freeze(0, 0, duration=2)

    def test_initialization(self):
        self.assertEqual(self.freeze.symbol, 'f')
        self.assertEqual(self.freeze.rect.x, 0)
        self.assertEqual(self.freeze.rect.y, 0)
        self.assertEqual(self.freeze.duration, 2)
        self.assertFalse(self.freeze.is_frozen)
        self.assertEqual(self.freeze.freeze_start_time, 0)

    def test_freeze_player(self):
        self.freeze.freeze_player(self.player_mock)
        self.assertTrue(self.freeze.is_frozen)
        self.freeze.freeze_player(self.player_mock)  # Should not freeze again
        self.assertTrue(self.freeze.is_frozen)

    @unittest.mock.patch('builtins.print')
    def test_update(self, mock_print):
        # Freeze the player
        self.freeze.freeze_player(self.player_mock)
        # Wait for the freeze duration to elapse
        time.sleep(3)
        self.freeze.update()
        self.assertFalse(self.freeze.is_frozen)
        mock_print.assert_called_with("Player unfrozen!")

if __name__ == '__main__':
    unittest.main()
"""

#The Freeze class encapsulates its data (position, duration, is_frozen, freeze_start_time) and behavior (freeze_player, update methods) together.
#The attributes are not encapsulated with access modifiers.