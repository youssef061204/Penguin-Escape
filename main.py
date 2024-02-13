
"""
File: main.py
Date completed: 01/17/2023
The main file of the project.
"""
import sys
import pygame

from pygame.locals import *
from pygame.locals import QUIT

from hardmode import HardMode
from CONSTANTS import *
from menu import Menu


file = True
pygame.init()
pygame.font.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
start_button = Menu(WIDTH//2 - 35, 3*HEIGHT//4+27,STARTIMG)
exit_button = Menu(WIDTH//2 + 25 , 3*HEIGHT//4+25,EXITIMG)

pygame.display.set_caption("game")
hard_mode = HardMode()  # Create an instance of HardMode to access p1
#texts = Text(SCREEN)

exit_button.press(SCREEN)
start_button.press(SCREEN)
while True:

    # Check for player input.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hard_mode.player.move(-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                hard_mode.player.move(GRID_SIZE, 0)
            elif event.key == pygame.K_UP:
                hard_mode.player.move(0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN:
                hard_mode.player.move(0, GRID_SIZE)
            elif event.key == pygame.K_r:
                hard_mode.player.resetLevel()

    # Check if the player has beaten the game.
    if hard_mode.player.levelNum >= len(LEVELS):
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(GGIMG, (0,0))
        pygame.display.flip()
        pygame.display.update()
        continue

    # Check if the player is still on the start screen.
    if file == True:
        SCREEN.fill((52,78,91))
        SCREEN.blit(pygame.transform.scale(pygame.image.load(
            "assets/startbg.png"),(WIDTH, HEIGHT)), (0,0))
        #texts.draw_text("Penguino", text_font, (0, 0, 0), 220, 150)
        
        if exit_button.press(SCREEN):
            pygame.quit()
            sys.exit()
        if start_button.press(SCREEN):
            file = False
    else:    
        # Move the player and the enemy, draw stuff
        hard_mode.update()
        hard_mode.draw(SCREEN)
        hard_mode.health_manager.draw_hearts(SCREEN)
    
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
    pygame.display.update()
