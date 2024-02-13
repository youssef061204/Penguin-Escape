
"""
Author: Daniel Chen
File: player.py
Date completed: 01/16/2023
Creates a movable player object that the user controls.
"""
import pygame
import unittest

from CONSTANTS import GRID_SIZE, PLAYERPOS, WIDTH, HEIGHT, STARSPERLEVEL
from level import Level
from portal import Portal
from freeze import Freeze
from button import Button, DestroyableButton
from health_manager import HealthManager
from krill import Krill


class Player:
    """
    A Player object controlled by the user which moves around in the 
    level,interacting with objects inside.

    Attributes:
        image (pygame.Surface): The image of the player.
        levelNum (int): The number of the current level.
        level (Level): The level object of the current level.
        freeze (Freeze): Controls when the player is frozen.
        health_manager (HealthManager): Controls the player's health.
        levelChanged (boolean): Checks if the level has recently been changed.
    """

    def __init__(self):
        """Setup the player object."""
        self.image = pygame.transform.scale(
            pygame.image.load("assets/penguin.png"), (GRID_SIZE, GRID_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = PLAYERPOS[0][0]
        self.rect.y = PLAYERPOS[0][1]
        self.levelNum = 0
        self.level = Level(self.levelNum)  # Set to first level by default.
        self.freeze = Freeze(0, 0, duration=2)  # Add Freeze instance.
        self.health_manager = HealthManager(3)
        self.levelChanged = True

    def move(self, dx, dy):
        """
        Move the player by the given amount.

        Args:
            dx (int): The amount to move the player horizontally.
            dy (int): The amount to move the player vertically.
        """
        # Check if player goes off screen.
        if self.rect.x + dx < 0 or self.rect.x + dx >= WIDTH:
            return
        if self.rect.y + dy < 0 or self.rect.y + dy >= HEIGHT:
            return

        # Move if the square ahead is not blocked.
        ahead = self.level.checkSquare(self.rect.x + dx, self.rect.y + dy)
        if ahead != "w" and ahead != "l":

            if not self.freeze.is_frozen:

                # Place lava on previous tile if possible.
                if not (type(self.level.checkSquare(self.rect.x,self.rect.y))
                        is Portal or 
                        type(self.level.checkSquare(self.rect.x,self.rect.y)) 
                        is Button):
                    self.level.changeSquare(self.rect.x, self.rect.y, "l")

                self.rect.x += dx
                self.rect.y += dy

                # Check if the player triggered an effect.
                if type(ahead) is Portal:
                    ahead.teleport(self)
                elif type(ahead) is Freeze:
                    self.freeze.freeze_player(self)
                elif (type(ahead) is Button or type(ahead) 
                      is DestroyableButton):
                    ahead.activate(self.level)

                krill = self.level.checkSquare(self.rect.x, self.rect.y)
                if type(krill) is Krill:
                    krill.apply_effect()
                else:
                    self.level.starDisappear(self.rect.x, self.rect.y)

                    # If all stars are collected, move to next level.
                    if self.level.getStarsNum() == 0:
                        if self.levelNum >= len(STARSPERLEVEL) - 1:
                            self.levelNum += 1
                            return
                        self.setLevel(self.levelNum + 1)

    def __refresh(self):
        """Refresh the current level."""
        self.level = Level(self.levelNum)
        self.rect.x = PLAYERPOS[self.levelNum][0]
        self.rect.y = PLAYERPOS[self.levelNum][1]

    def setLevel(self, newLevel):
        """
        Set the current level to the given level number.

        Args:
            newLevel (int): The number of the new level.
        """
        self.levelNum = newLevel
        self.__refresh()
        self.levelChanged = True

    def resetLevel(self):
        """Reset the current level."""
        self.level.resetLava()
        self.__refresh()

    def update(self):
        """Update the freeze effect on the player."""
        self.freeze.update()

    def heal(self):
        """Heal the player."""
        self.health_manager.heal()


class TestPlayer(unittest.TestCase):
    """A list of tests for the Player class."""

    def runTest(self):
        """Setup the unit tests."""
        p1 = Player()
        self.assertEqual(p1.levelNum, 0, "incorrect level")
        self.assertEqual(p1.rect.x, 7 * GRID_SIZE, "wrong x pos")
        self.assertEqual(p1.rect.y, 3 * GRID_SIZE, "wrong y pos")

        p1.move(20, 0)
        self.assertEqual(p1.rect.x, 7 * GRID_SIZE + 20, "wrong x move")
        p1.move(0, 20)
        self.assertEqual(p1.rect.y, 3 * GRID_SIZE, "wrong y move")
        p1.move(WIDTH, 0)
        self.assertEqual(p1.rect.x, 7 * GRID_SIZE + 20, "went off screen")
        p1.move(0, HEIGHT)
        self.assertEqual(p1.rect.y, 3 * GRID_SIZE, "went off screen")

        p1.resetLevel()
        self.assertEqual(p1.rect.x, 7 * GRID_SIZE, "wrong x pos")
        self.assertEqual(p1.rect.y, 3 * GRID_SIZE, "wrong y pos")


# Run unit tests.
"""
test_player_suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
runner = unittest.TextTestRunner()
runner.run(test_player_suite)
"""
