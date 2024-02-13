"""
Author: Youssef Elsokkary
File: hardmode.py
Date completed: 1/17/2024
Creates a hardmode version of the game designed for experienced players, includes enemies, heals, and health.
"""

import unittest

import pygame
import sys
from pygame.locals import QUIT
from player import Player
from enemy import Enemy
from krill import Krill
from health_manager import HealthManager
from CONSTANTS import *
from menu import Menu

class HardMode:
    def __init__(self):
        """
        Initialize the HardMode game mode.

        Attributes:
        - player: Player object representing the main character.
        - health_manager: HealthManager object managing player health.
        - enemies: List of Enemy objects representing enemies.
        - krills: List of Krill objects representing healing items.
        """
        self.player = Player()
        self.health_manager = HealthManager(5)
        self.enemies = [Enemy(100, 100, self.player, self.health_manager)]
        self.krills = [Krill(200, 200, self.player)]

    def update(self):
        """
        Update the game state.

        Check for collisions with krill and enemies, apply effects,
        and update the player level.
        """
        self.player.freeze.update()

        # Check for collision with krill and apply healing
        for krill in self.krills:
            if pygame.sprite.collide_rect(self.player, krill):
                krill.apply_effect()
                krill.kill()
                self.health_manager.heal()
                #print("Player healed!")

        # Check for collision with enemies
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.player, enemy):
                enemy.handle_collision()
                self.health_manager.decrement_health()

        # Update enemy movement and handle collisions
        for enemy in self.enemies:
            enemy.move()
            enemy.handle_collision()

        # If the level changed, update position of krill.
        if self.player.levelChanged:
            for krill in self.krills:
                krill.moveTo(PLAYERPOS[self.player.levelNum][0],
                             PLAYERPOS[self.player.levelNum][1])

            self.player.levelChanged = False

        self.reset_player_level()

    def draw(self, screen):
        """
        Draw the game elements on the screen.

        Args:
        - screen: Pygame display surface.
        """
        # Draw the player, enemies, krills, and health bar
        screen.fill((255, 255, 255))
        self.player.level.displayLevel(screen)
        screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        for enemy in self.enemies:
            screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
        for krill in self.krills:
            screen.blit(krill.image, (krill.rect.x, krill.rect.y))
        self.health_manager.draw_hearts(screen)

    def is_player_dead(self):
        """
        Check if the player is dead.

        Returns:
        - True if player health is zero or less, False otherwise.
        """
        return self.health_manager.health <= 0

    def reset_player_level(self):
        """
        Reset the player's level and health if they are dead.
        """
        if self.is_player_dead():
            self.player.setLevel(0)  # Reset the player's level to 0
            self.health_manager.health = self.health_manager.max_health
            self.health_manager.spawn_hearts()
            print("Player died! Respawning...")
"""
# Uncomment the following when you want to run the unittests

class TestHardMode(unittest.TestCase):
    def setUp(self):
        self.hard_mode = HardMode()

    def test_player_initialization(self):
        self.assertIsInstance(self.hard_mode.player, Player)

    def test_health_manager_initialization(self):
        self.assertIsInstance(self.hard_mode.health_manager, HealthManager)
        self.assertEqual(self.hard_mode.health_manager.health, 5)

    def test_enemy_initialization(self):
        self.assertEqual(len(self.hard_mode.enemies), 1)
        self.assertIsInstance(self.hard_mode.enemies[0], Enemy)

    def test_krill_initialization(self):
        self.assertEqual(len(self.hard_mode.krills), 1)
        self.assertIsInstance(self.hard_mode.krills[0], Krill)

    def test_update_method(self):
        self.hard_mode.player.rect.x = 200
        self.hard_mode.player.rect.y = 200
        self.hard_mode.enemies[0].rect.x = 200
        self.hard_mode.enemies[0].rect.y = 200

        self.hard_mode.update()
        self.assertEqual(self.hard_mode.health_manager.health, 4)

    def test_is_player_dead_method(self):
        self.assertFalse(self.hard_mode.is_player_dead())
        self.hard_mode.health_manager.health = 0
        self.assertTrue(self.hard_mode.is_player_dead())

    def test_reset_player_level_method(self):
        self.hard_mode.health_manager.health = 0
        self.hard_mode.reset_player_level()
        self.assertEqual(self.hard_mode.player.level.current_level, 0)
        self.assertEqual(self.hard_mode.health_manager.health, self.hard_mode.health_manager.max_health)

if __name__ == '__main__':
    unittest.main()
"""

#The HardMode class encapsulates player, health_manager, enemies, and krills within its instance.
#However, the attributes of Player, HealthManager, Enemy, and Krill classes themselves are not explicitly encapsulated with access modifiers.
#The update and draw methods in the HardMode class encapsulate the logic related to updating the game state and drawing elements.