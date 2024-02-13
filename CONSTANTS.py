
"""
File: CONSTANTS.py
Date completed: 01/16/2023
Stores all of the data used in the program.
"""

import pygame
WIDTH, HEIGHT = 400, 400
GRID_SIZE = WIDTH // 10
FPS = 50
PLAYERPOS = [[7 * GRID_SIZE, 3 * GRID_SIZE], [8 * GRID_SIZE, 1 * GRID_SIZE],
             [2 * GRID_SIZE, 2 * GRID_SIZE], [7 * GRID_SIZE, 2 * GRID_SIZE],
             [5 * GRID_SIZE, 1 * GRID_SIZE], [9 * GRID_SIZE, 1 * GRID_SIZE],
             [5 * GRID_SIZE, 4 * GRID_SIZE], [7 * GRID_SIZE, 7 * GRID_SIZE],
             [6 * GRID_SIZE, 5 * GRID_SIZE], [7 * GRID_SIZE, 5 * GRID_SIZE],
             [8 * GRID_SIZE, 8 * GRID_SIZE], [6 * GRID_SIZE, 2 * GRID_SIZE],
             [7 * GRID_SIZE, 2 * GRID_SIZE], [3 * GRID_SIZE, 4 * GRID_SIZE],
             [7 * GRID_SIZE, 4 * GRID_SIZE]]
WALLIMG = pygame.transform.scale(pygame.image.load("assets/snow_wall.png"),
                                 (GRID_SIZE, GRID_SIZE))
STARIMG = pygame.transform.scale(pygame.image.load("assets/stars.png"),
                                 (GRID_SIZE, GRID_SIZE))
LAVAIMG = pygame.transform.scale(pygame.image.load("assets/lava.jpg"),
                                 (GRID_SIZE, GRID_SIZE))
PORTALIMG = pygame.transform.scale(pygame.image.load("assets/portal.jpg"),
                                   (GRID_SIZE, GRID_SIZE))
ENEMYIMG = pygame.transform.scale(pygame.image.load("assets/enemy.jpg"),
                                  (GRID_SIZE, GRID_SIZE))
FREEZEIMG = pygame.transform.scale(pygame.image.load("assets/freeze.jpg"),
                                   (GRID_SIZE, GRID_SIZE))

STARTIMG = pygame.transform.scale(pygame.image.load("assets/start1.png"),
                                  (GRID_SIZE, GRID_SIZE))

EXITIMG = pygame.transform.scale(pygame.image.load("assets/exit1.png"),
                                 (GRID_SIZE, GRID_SIZE))
BUTTONIMG = pygame.transform.scale(pygame.image.load("assets/button.png"),
                                   (GRID_SIZE, GRID_SIZE))
DBIMG = pygame.transform.scale(pygame.image.load("assets/button_green.png"),
                               (GRID_SIZE, GRID_SIZE))
KRILLIMG = pygame.transform.scale(pygame.image.load("assets/krill.jpg"),
                                  (GRID_SIZE, GRID_SIZE))
GGIMG = pygame.transform.scale(pygame.image.load("assets/gamewin.png"),
      (WIDTH, HEIGHT))


#text_font = pygame.font.SysFont("arial", 30)

#text_colour = (128,128,128)

# A list of the levels and stars.
STARSPERLEVEL = [1, 12, 8, 1, 3, 2, 6, 7, 5, 9, 24, 2, 3, 4, 5]
LEVELS = [
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "e", "b", "u", "b", "s", "w", "w"],
     ["w", "w", "w", "b", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "b", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "b", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "b", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "b", "b", "b", "s", "b", "b", "b", "w", "w"],
     ["w", "b", "w", "s", "w", "s", "w", "b", "w", "w"],
     ["w", "b", "s", "b", "b", "b", "s", "b", "w", "w"],
     ["w", "s", "w", "b", "w", "b", "w", "s", "w", "w"],
     ["w", "b", "s", "b", "b", "b", "s", "b", "w", "w"],
     ["w", "b", "w", "s", "w", "s", "w", "b", "w", "w"],
     ["w", "b", "b", "b", "s", "b", "b", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "s", "b", "s", "b", "b", "b", "s", "w", "w"],
     ["w", "b", "b", "b", "s", "w", "s", "b", "w", "w"],
     ["w", "w", "w", "b", "b", "b", "b", "b", "w", "w"],
     ["w", "w", "w", "s", "w", "s", "w", "b", "w", "w"],
     ["w", "w", "w", "b", "b", "b", "b", "s", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "p", "b", "b", "b", "b", "s", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "b", "b", "b", "b", "p", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "b", "b", "s", "b", "b", "w"],
     ["w", "w", "w", "w", "b", "w", "w", "w", "b", "w"],
     ["w", "b", "b", "b", "p", "b", "s", "b", "p", "w"],
     ["w", "w", "w", "w", "b", "w", "w", "w", "b", "w"],
     ["w", "w", "w", "w", "b", "b", "s", "b", "b", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "b", "b", "b", "b", "w", "w", "w"],
     ["w", "w", "w", "b", "w", "w", "b", "w", "w", "w"],
     ["w", "b", "b", "w", "s", "w", "b", "b", "s", "w"],
     ["w", "e", "w", "w", "b", "b", "b", "w", "b", "w"],
     ["w", "b", "w", "w", "w", "w", "b", "w", "b", "w"],
     ["w", "b", "w", "w", "e", "w", "w", "w", "b", "w"],
     ["w", "b", "w", "w", "b", "w", "b", "w", "b", "w"],
     ["w", "b", "w", "w", "b", "b", "b", "w", "b", "w"],
     ["w", "b", "b", "b", "b", "b", "b", "b", "b", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "b", "s", "b", "p", "w", "w", "w"],
     ["w", "w", "w", "b", "b", "b", "b", "w", "w", "w"],
     ["w", "e", "b", "b", "s", "w", "b", "b", "e", "w"],
     ["w", "w", "f", "b", "b", "b", "b", "w", "w", "w"],
     ["w", "w", "b", "b", "b", "b", "s", "f", "w", "w"],
     ["w", "e", "b", "b", "b", "b", "b", "b", "e", "w"],
     ["w", "w", "b", "b", "b", "b", "b", "b", "w", "w"],
     ["w", "w", "p", "s", "s", "s", "b", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "s", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "b", "s", "b", "s", "b", "s", "p", "w", "w"],
     ["w", "s", "b", "s", "b", "s", "b", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "b", "w", "w"],
     ["w", "b", "b", "b", "w", "b", "b", "b", "w", "w"],
     ["w", "p", "w", "b", "b", "b", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "s", "b", "b", "p", "b", "b", "b", "w", "w"],
     ["w", "b", "s", "w", "s", "w", "w", "s", "w", "w"],
     ["w", "s", "b", "b", "b", "b", "b", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "b", "b", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "b", "p", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "s", "b", "b", "s", "b", "w", "w", "w"],
     ["w", "w", "b", "s", "w", "w", "b", "s", "w", "w"],
     ["w", "w", "b", "s", "s", "b", "s", "w", "w", "w"],
     ["w", "w", "s", "b", "b", "s", "p", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "b", "b", "d", "w", "w"],
     ["w", "w", "w", "w", "w", "b", "p", "b", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "b", "s", "b", "s", "b", "s", "b", "w", "w"],
     ["w", "s", "w", "s", "w", "s", "w", "s", "w", "w"],
     ["w", "b", "s", "b", "s", "b", "s", "b", "w", "w"],
     ["w", "s", "w", "s", "w", "s", "w", "s", "w", "w"],
     ["w", "b", "s", "b", "s", "b", "s", "b", "w", "w"],
     ["w", "s", "w", "s", "w", "s", "w", "s", "w", "w"],
     ["w", "b", "s", "b", "s", "b", "s", "u", "b", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "b", "b", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "u", "l", "p", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "b", "s", "p", "s", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "s", "b", "b", "w", "w", "w", "w", "w"],
     ["w", "w", "l", "w", "b", "w", "w", "w", "w", "w"],
     ["w", "w", "d", "w", "b", "w", "w", "s", "w", "w"],
     ["w", "w", "l", "w", "p", "w", "w", "b", "w", "w"],
     ["w", "w", "b", "b", "p", "b", "s", "d", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "p", "u", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "b", "w", "w", "w", "w", "w"],
     ["w", "w", "b", "b", "b", "b", "b", "w", "w", "w"],
     ["w", "w", "s", "b", "b", "b", "s", "w", "w", "w"],
     ["w", "w", "w", "w", "b", "w", "w", "w", "w", "w"],
     ["w", "w", "s", "b", "b", "b", "s", "w", "w", "w"],
     ["w", "w", "b", "b", "b", "b", "b", "w", "w", "w"],
     ["w", "w", "w", "w", "p", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
    [["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "s", "p", "s", "w", "w", "w", "w"],
     ["w", "w", "w", "s", "p", "s", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "u", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "b", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "b", "l", "b", "s", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
     ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]],
]