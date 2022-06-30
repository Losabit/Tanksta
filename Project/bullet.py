import pygame
import os
import math

directory = str(os.path.abspath(os.getcwd())) + '/'  # '/Project/'


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordonates, angle, puissance):
        puissance = puissance * 19
        self.image = pygame.image.load(
            directory + 'assets/objects/tank_bullet5.png')
        self.origin_image = self.image
        self.rect = coordonates
        self.image = pygame.transform.rotate(self.origin_image, angle)
        self.angle = angle
        self.damage = 20
        self.puissance = puissance

        self.vx = puissance * math.cos(math.radians(angle))
        self.vy = puissance * math.sin(math.radians(angle))

        self.ax = 0  # puissance # vent
        self.ay = -9.8

        self.x = self.rect[0]
        self.y = self.rect[1]
        self.time = 0

    def updateVx(self, dt):
        self.vx = self.vx + self.ax * dt
        return self.vx

    def updateVy(self, dt):
        self.vy = self.vy + self.ay * dt
        return self.vy

    def updateX(self, dt):
        self.x = self.x + 0.5 * (self.vx + self.updateVx(dt)) * dt
        return self.x

    def updateY(self, dt):
        self.y = self.y - 0.5 * (self.vy + self.updateVy(dt)) * dt
        return self.y

    def updateBulletPosition(self, dt):
        self.rect[0] = self.updateX(dt)
        self.rect[1] = self.updateY(dt)
        self.time = self.time + dt

    def display(self, screen, delta):
        screen.blit(self.image, self.rect)
        self.updateBulletPosition(delta)
