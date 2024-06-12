# Imports.

import pygame
import random

class Racket:
    def __init__(self, x, y, width, height, dy, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = dy
        self.screen_height = screen_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.dy
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen_height:
            self.rect.y += self.dy

    def move_ai(self, ball_y):
        if self.rect.centery < ball_y:
            self.rect.y += self.dy
        elif self.rect.centery > ball_y:
            self.rect.y -= self.dy

    def constrain(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Ball:
    def __init__(self, x, y, size, velocity_x, velocity_y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.size = size
        self.initial_velocity_x = velocity_x
        self.initial_velocity_y = velocity_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = self.random_color()

    def move(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def bounce(self):
        self.velocity_x = -self.velocity_x
        self.color = self.random_color()

    def bounce_vertical(self):
        self.velocity_y = -self.velocity_y
        self.color = self.random_color()

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = -self.initial_velocity_x if self.velocity_x > 0 else self.initial_velocity_x
        self.velocity_y = self.initial_velocity_y

    def reset_velocity(self):
        self.velocity_x = self.initial_velocity_x
        self.velocity_y = self.initial_velocity_y

    def increase_speed(self):
        if pygame.time.get_ticks() % 10000 < 50:  # Aumenta a velocidade a cada 10 segundos.
            self.velocity_x *= 1.1
            self.velocity_y *= 1.1

    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))