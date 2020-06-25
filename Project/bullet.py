import pygame
import os

directory = str(os.path.abspath(os.getcwd()))  + '/Project/'

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordonates, angle, puissance):
        self.image = pygame.image.load(directory + 'assets/objects/tank_bullet5.png')
        self.origin_image = self.image
        self.rect = coordonates
        self.image = pygame.transform.rotate(self.origin_image, angle)
        #self.canon_rect = self.canon_image.get_rect(center= self.canon_rect.center)
        self.puissance = puissance
        
    def display(self, screen):
        screen.blit(self.image, self.rect)