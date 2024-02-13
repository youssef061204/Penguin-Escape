"""#unfinished
import pygame
import sys
from pygame.locals import QUIT
from player import Player
from enemy import Enemy
from krill import Krill
from health_manager import HealthManager
from CONSTANTS import *
from menu import Menu
class NormalMode:
    def __init__(self):
        self.player = Player()
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.player.level.displayLevel(screen)
        screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))"""