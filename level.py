
"""
Author: Daniel Chen
File: level.py
Date completed: 01/16/2023
Creates a level object storing a 2D position array of the map 
with various functions.
"""
import unittest

from CONSTANTS import *
from portal import Portal
from enemy import Enemy
from freeze import Freeze
from button import Button, DestroyableButton
from krill import Krill


class Level:
    """
    A class which tracks general information about each level.

    Attributes:
        _starsLeft (int): The number of stars left in the level.
        enemies (list): A list of enemies in the level.
        level (list): A 2D array of the objects in the level.

    Legend for squares:
        b --> blank
        p --> portal
        w --> wall
        s --> star
        l --> lava
        f --> freeze
        u --> button
        d --> destroyable button
    """

    def __calculatePos(self, i, j):
        """
        Calculates the x and y coordinates of a square in the level 
        based on its array indices.

        Args:
            i (int): The row index of the square.
            j (int): The column index of the square.

        Returns:
            tuple: The pygame coordinates of the square.
        """

        return (i * GRID_SIZE), (j * GRID_SIZE)

    def __convertPos(self, x, y):
        """
        Converts a pygame coordinate to a 2D array index.

        Args:
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.

        Returns:
            tuple: The array indices of the square.
        """
        return x // GRID_SIZE, y // GRID_SIZE

    def __init__(self, levelNum):
        """
        Initialize the 2D array of the level.

        Args:
            levelNum (int): The number of the level. 
        """
        # Make a copy of the layout of current level.
        newLevel = LEVELS[levelNum]
        
        # Setup the size of 2D array.
        self.level = [[None for _ in range(len(newLevel[0]))] 
                      for _ in range(len(newLevel))]
        self._starsLeft = STARSPERLEVEL[levelNum]
        self.enemies = []  # Store enemy positions.

        # Add objects to the level.
        p1 = 0
        for i in range(len(newLevel)):
            for j in range(len(newLevel[i])):
                
                if newLevel[i][j] == 'p':
                    if p1 == 0:
                        # Save the position of the first portal.
                        p1 = [i, j]
                    else:
                        # Use the save position to initialize portal objects.
                        self.level[p1[0]][p1[1]] = Portal(
                            p1[0] * GRID_SIZE, p1[1] * GRID_SIZE, 
                            i * GRID_SIZE, j * GRID_SIZE)
                        self.level[i][j] = Portal(i * GRID_SIZE, 
                                                  j * GRID_SIZE, 
                                                  p1[0] * GRID_SIZE, 
                                                  p1[1] * GRID_SIZE)
                elif newLevel[i][j] == 'f':
                    self.level[i][j] = Freeze(i * GRID_SIZE, j * GRID_SIZE)
                elif newLevel[i][j] == "u":
                    self.level[i][j] = Button(i * GRID_SIZE, j * GRID_SIZE)
                elif newLevel[i][j] == "d":
                    self.level[i][j] = DestroyableButton(i * GRID_SIZE, 
                                                         j * GRID_SIZE)
                else:
                    self.level[i][j] = newLevel[i][j]

    def displayLevel(self, screen):
        """
        Displays the level on the screen.

        Args:
            screen (pygame.Surface): The screen to display the level on.
        """
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                # Find the correct image and display it.
                if self.level[i][j] == "w":
                    screen.blit(WALLIMG, self.__calculatePos(i, j))
                elif self.level[i][j] == "s":
                    screen.blit(STARIMG, self.__calculatePos(i, j))
                elif self.level[i][j] == "l":
                    screen.blit(LAVAIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is Portal:
                    screen.blit(PORTALIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is Enemy:
                    screen.blit(ENEMYIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is Freeze:
                    screen.blit(FREEZEIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is Button:
                    screen.blit(BUTTONIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is DestroyableButton:
                    screen.blit(DBIMG, self.__calculatePos(i, j))
                elif type(self.level[i][j]) is Krill:
                    screen.blit(KRILLIMG, self.__calculatePos(i, j))

    def checkSquare(self, x, y):
        """
        Checks to see what object is on a square in the level.

        Args:
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.

        returns:
            str/object: The object on the square.
        """
        converted = self.__convertPos(x, y)
        return self.level[converted[0]][converted[1]]

    def changeSquare(self, x, y, new):
        """
        Changes the content of a square in the level.

        Args:
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            new (str): The new content of the square.
        """
        converted = self.__convertPos(x, y)
        self.level[converted[0]][converted[1]] = new

    def starDisappear(self, x, y):
        """
        Deletes a star from the level if it touches the player.

        Args:
            x (int): The x coordinate of the player.
            y (int): The y coordinate of the player.
        """
        converted = self.__convertPos(x, y)
        if self.checkSquare(x, y) == "s":
            # Change square to blank, decrement number of stars left.
            self.level[converted[0]][converted[1]] = "b"
            self._starsLeft -= 1
            print(self._starsLeft)

    def resetLava(self):
        """
        Reset all of the lava in the level.
        """
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                # Check if the square is lava.
                if self.level[i][j] == "l":
                    self.level[i][j] = "b"

    def getStarsNum(self):
        """
        Determine the number of stars left in the level.

        returns:
            int: The number of stars left in the level.
        """
        return self._starsLeft


class TestLevel(unittest.TestCase):
    """A list of tests for the Level class."""

    def runTest(self):
        """Setup the unit tests."""
        le = Level(0)
        self.assertEqual(le.checkSquare(GRID_SIZE,GRID_SIZE), "w", 
                         "level not loaded")
        le.changeSquare(GRID_SIZE,GRID_SIZE,"l")
        self.assertEqual(le.checkSquare(GRID_SIZE,GRID_SIZE), "l", 
                         "square not changed")
        le.resetLava()
        self.assertEqual(le.checkSquare(GRID_SIZE,GRID_SIZE), "b", 
                         "lava not removed")

        le = Level(7)
        self.assertEqual(le._starsLeft, 7, "stars not loaded")
        self.assertEqual(le.checkSquare(4*GRID_SIZE,4*GRID_SIZE), "s", 
                         "star not there")
        le.starDisappear(4*GRID_SIZE,4*GRID_SIZE)
        self.assertEqual(le._starsLeft, 6, "star not decremented")
        self.assertEqual(le.checkSquare(4*GRID_SIZE,4*GRID_SIZE), "b", 
                         "star not removed")


# Run unit tests.
"""
test_level_suite = unittest.TestLoader().loadTestsFromTestCase(TestLevel)
runner = unittest.TextTestRunner()
runner.run(test_level_suite)
"""
