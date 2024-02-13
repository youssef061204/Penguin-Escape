"""
Author: Michael Jin
File: menu_test.py
Date completed: 1/17/2024
Unittest of menu.py file
"""

"""
python -m unittest menu_test.py
import pygame
import unittest
from unittest.mock import Mock
from menu import Menu  # Original file


class TestMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = Mock()
        self.image = pygame.Surface((50, 30))  # Mock image for testing
        self.menu = Menu(100, 100, self.image)

    def test_button_click_detection(self):
        # Simulate mouse click on the button
        pygame.mouse.get_pos = Mock(return_value=(110, 110))
        pygame.mouse.get_pressed = Mock(return_value=(1, 0, 0))  

        # Call the draw method to check for button click
        action = self.menu.press(self.screen)

        # Assert that the action is True (button click detected)
        self.assertTrue(action)

if __name__ == '__main__':
    unittest.main()
"""