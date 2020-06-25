import pygame
import math
import os
from bullet import Bullet

directory = str(os.path.abspath(os.getcwd()))  + '/Project/'

class Tank(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__

        self.body_image = pygame.image.load(directory + 'assets/objects/tanks_tankGreen_body3.png')
        self.body_rect = self.body_image.get_rect()
        self.body_rect.x = position[0]
        self.body_rect.y = position[1]

        self.wheel_image = pygame.image.load(directory + 'assets/objects/tanks_tankTracks3.png')
        self.wheel_rect = self.wheel_image.get_rect()
        self.wheel_rect.x = position[0] + 5
        self.wheel_rect.y = position[1] + 40

        self.canon_image = pygame.image.load(directory + 'assets/objects/tanks_turret4.png')
        self.canon_rect = self.canon_image.get_rect()
        self.canon_image = pygame.transform.scale(self.canon_image, tuple([int(self.canon_rect.w * 1.5), self.canon_rect.h * 2]))
        self.canon_rect = self.canon_image.get_rect()
        self.canon_rect.x = position[0] + 15
        self.canon_rect.y = position[1] + 5
        self.canon_originImage = self.canon_image
        self.canon_angle = 0

        self.bullets = []

    def display(self, screen):
        screen.blit(self.canon_image, self.canon_rect)
        screen.blit(self.wheel_image, self.wheel_rect)
        screen.blit(self.body_image, self.body_rect)
        for bullet in self.bullets:
            bullet.display(screen)

    def moveCanon(self, value):
        self.canon_angle += value
        self.canon_image = pygame.transform.rotate(self.canon_originImage, self.canon_angle)
        self.canon_rect = self.canon_image.get_rect(center= self.canon_rect.center)

    def shoot(self, puissance):
        coordonates = list(self.canon_rect.center)
        coordonates[0] += math.cos(math.radians(self.canon_angle)) * 30
        coordonates[1] -= math.sin(math.radians(self.canon_angle)) * 30 + 5
        self.bullets.append(Bullet(coordonates, self.canon_angle, puissance))

    def move(self, value):
        self.wheel_rect.x += value
        self.body_rect.x += value
        self.canon_rect.x += value