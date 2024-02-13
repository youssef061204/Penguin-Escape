"""
Author: Youssef Elsokkary
File: enemy.py
Date completed: 1/17/2024
Creates a Ghost enemy that chases you through levels.
"""

from unittest.mock import Mock
import pygame
from game_object import GameObject
from CONSTANTS import GRID_SIZE, WIDTH, HEIGHT
from health_manager import HealthManager

class Enemy(GameObject):
    def __init__(self, x, y, player, health_manager):
        """
        Initialize an Enemy.

        Args:
        - x: X-coordinate of the enemy's position.
        - y: Y-coordinate of the enemy's position.
        - player: Player object representing the main character.
        - health_manager: HealthManager object managing player health.
        """
        super().__init__('e', x, y)
        self.speed = 1  # Adjust the speed as needed
        self.image = pygame.transform.scale(pygame.image.load("assets/enemy.jpg"), (GRID_SIZE, GRID_SIZE))
        self.player = player
        self.health_manager = health_manager

    def check_collision(self):
        """
        Check for collisions with the player.

        Returns:
        - True if a collision is detected, False otherwise.
        """
        if self.rect.colliderect(self.player.rect):
            return True
        return False

    def move(self):
        """
        Move the enemy towards the player.
        """
        # Calculate the direction towards the player
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y

        # Normalize the direction vector
        length = max(1, abs(dx) + abs(dy))
        dx = (dx / length) * self.speed
        dy = (dy / length) * self.speed

        # Calculate the potential new position
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Update the enemy's position
        self.rect.x = new_x
        self.rect.y = new_y

        # Ensure the enemy stays within the level boundaries
        self.rect.x = max(0, min(self.rect.x, WIDTH - GRID_SIZE))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - GRID_SIZE))

    def handle_collision(self):
        """
        Handle collisions with the player.

        Decrement player health if a collision is detected.
        """
        if self.check_collision():
            self.health_manager.decrement_health()


"""
# Uncomment the following when you want to run the unittests
import unittest
from unittest.mock import Mock

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.player_mock = Mock()
        self.health_manager_mock = Mock()
        self.enemy = Enemy(0, 0, self.player_mock, self.health_manager_mock)

    def test_initialization(self):
        self.assertEqual(self.enemy.symbol, 'e')
        self.assertEqual(self.enemy.rect.x, 0)
        self.assertEqual(self.enemy.rect.y, 0)
        self.assertEqual(self.enemy.image.get_size(), (GRID_SIZE, GRID_SIZE))
        self.assertEqual(self.enemy.player, self.player_mock)
        self.assertEqual(self.enemy.health_manager, self.health_manager_mock)

    def test_check_collision(self):
        # Mocking collision between enemy and player
        self.enemy.rect.x = 10
        self.enemy.rect.y = 10
        self.player_mock.rect.x = 10
        self.player_mock.rect.y = 10
        self.assertTrue(self.enemy.check_collision())

        # No collision when player is far away
        self.player_mock.rect.x = 100
        self.player_mock.rect.y = 100
        self.assertFalse(self.enemy.check_collision())

    def test_move(self):
        # Test movement (Note: actual movement logic is complex and may need more comprehensive testing)
        self.enemy.move()

    def test_handle_collision(self):
        # Mocking collision between enemy and player
        self.enemy.rect.x = 10
        self.enemy.rect.y = 10
        self.player_mock.rect.x = 10
        self.player_mock.rect.y = 10

        self.enemy.handle_collision()
        self.health_manager_mock.decrement_health.assert_called_once()

        # No collision, health manager should not be called
        self.enemy.rect.x = 100
        self.enemy.rect.y = 100
        self.enemy.handle_collision()
        self.health_manager_mock.decrement_health.assert_called_once()

if __name__ == '__main__':
    unittest.main()
"""