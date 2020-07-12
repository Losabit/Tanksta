import pygame
import math
import os
from bullet import Bullet

directory = str(os.path.abspath(os.getcwd()))  + '/' #'/Project/'

class Tank(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__
        self.health = 100
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

    def display(self, screen, tanks):
        screen.blit(self.canon_image, self.canon_rect)
        screen.blit(self.wheel_image, self.wheel_rect)
        screen.blit(self.body_image, self.body_rect)
        for i in range(len(self.bullets)):
            if i == len(self.bullets):
                i -= 1
            bullet = self.bullets[i]
            bullet.display(screen)
            if bullet.rect[1] > 710:
                del self.bullets[i]
            elif bullet.rect[0] > 1500 or bullet.rect[0] < -500:
                del self.bullets[i]
            else:
                for tank_ennemi in tanks:
                    if abs(bullet.rect[0] - tank_ennemi.body_rect.x) < 30 and abs(bullet.rect[1] - tank_ennemi.body_rect.y) < 30:
                        tank_ennemi.touched(bullet.damage)
                        del self.bullets[i]


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

    def touched(self, value):
        self.health -= value