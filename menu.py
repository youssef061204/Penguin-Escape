"""
Author: Michael Jin
File: menu.py
Date completed: 1/17/2024
Makes a starting menu when running this program
"""

import pygame
import unittest
from unittest.mock import Mock


class Menu():
    def __init__(self,x,y,image):
        """
        Initialize a Menu object.

        Args:
            x (int): x-coordinate of the menu button.
            y (int): y-coordinate of the menu button.
            image(str): Address of the image.
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
 

    def press(self,Screen):
        """
        Check the button whether was pressed or not.

        Args:
            Screen(str): the screen that the program is using.

        Returns:
            action(bool): whether the button is pressed or not.
        """
        action = False
        pos = pygame.mouse.get_pos() # Position of current mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 \
            and self.clicked == False:

                action = True # Record the state of action
                self.clicked = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        Screen.blit(self.image,self.rect)

        return action # Return True or False


        