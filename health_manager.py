"""
Author: Youssef Elsokkary
File: health_manager.py
Date completed: 1/17/2024
Manages all health functions; Adding and removing hearts/health.
"""

import unittest

import pygame
from CONSTANTS import GRID_SIZE, WIDTH
import time

class Health(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Initialize a Health object.

        Args:
        - x: X-coordinate of the heart's position.
        - y: Y-coordinate of the heart's position.
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/heart.png"), (GRID_SIZE, GRID_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """
        Draw the heart on the screen.

        Args:
        - screen: Pygame display surface.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def remove_heart(self):
        """
        Remove the heart from the sprite group.
        """
        self.kill()

class HealthManager:
    def __init__(self, max_health):
        """
        Initialize the HealthManager.

        Args:
        - max_health: Maximum health the player can have.
        """
        self.max_health = max_health
        self.health = max_health
        self.hearts = pygame.sprite.Group()
        self.spawn_hearts()
        self.last_hit_time = 0
        self.hit_cooldown = 1 

    def spawn_hearts(self):
        """
        Spawn heart sprites based on the player's health.
        """
        for i in range(self.health):
            heart = Health(WIDTH - (i + 1) * GRID_SIZE, 0)
            self.hearts.add(heart)

    def heal(self):
        """
        Increment the player's health and spawn a new heart sprite if not at max health.
        """
        if self.health < self.max_health:
            self.health = self.health + 1
            heart = Health(WIDTH - (self.health) * GRID_SIZE, 0)
            self.hearts.add(heart)
            print("Heart added.")

    def decrement_health(self):
        """
        Decrement the player's health, remove a heart sprite, and apply hit cooldown.
        """
        current_time = time.time()

        if current_time - self.last_hit_time > self.hit_cooldown:
            if self.health > 0 and len(self.hearts) > 0:
                # Remove a heart when health is decremented
                heart_to_remove = self.hearts.sprites()[-1]
                heart_to_remove.remove_heart()
                self.health -= 1

                # Update the last hit time
                self.last_hit_time = current_time
                print("Heart removed.")

    def draw_hearts(self, screen):
        """
        Draw all the heart sprites on the screen.

        Args:
        - screen: Pygame display surface.
        """
        self.hearts.draw(screen)
"""
class TestHealth(unittest.TestCase):
    def test_health_init(self):
        health = Health(0, 0)
        self.assertIsInstance(health, pygame.sprite.Sprite, "Health should be a pygame sprite")
        self.assertEqual(health.rect.x, 0, "Initial x-coordinate should be 0")
        self.assertEqual(health.rect.y, 0, "Initial y-coordinate should be 0")

class TestHealthManager(unittest.TestCase):
    def test_health_manager_init(self):
        health_manager = HealthManager(3)
        self.assertEqual(health_manager.max_health, 5, "Max health should be 5")
        self.assertEqual(health_manager.health, 5, "Initial health should be equal to max health")
        self.assertIsInstance(health_manager.hearts, pygame.sprite.Group, "Hearts should be a pygame sprite group")

    def test_heal(self):
        health_manager = HealthManager(3)
        health_manager.heal()
        self.assertEqual(health_manager.health, 3, "Health should not exceed max health initially")
        self.assertEqual(len(health_manager.hearts.sprites()), 3, "Number of hearts should not change initially")

        health_manager.health = 2
        health_manager.heal()
        self.assertEqual(health_manager.health, 5, "Health should be incremented")
        self.assertEqual(len(health_manager.hearts.sprites()), 5, "A new heart should be added")

    # Add more test methods for other HealthManager class functionalities if needed

if __name__ == '__main__':
    unittest.main()
"""