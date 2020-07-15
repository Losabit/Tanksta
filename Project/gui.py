import pygame
import pygame_gui
from tank import Tank

class GUI():
    def __init__(self,Tanks,manager):
        self.tanks =  Tanks
        self.manager = manager

    def drawHealthBar(self,screen):
        for tank in self.tanks:
            pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect((tank.body_rect.x, tank.body_rect.y - 100), (100, 50)),manager=self.manager,sprite_to_monitor=tank);

    def drawCurrentTurn(self,turn,screen):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        # now print the text
        text_surface = font.render(f'Player Turn:{str(turn)}' , True, pygame.Color('orange'))
        screen.blit(text_surface, dest=(1600/2,55))

    def draw(self,turn,screen):
        self.drawHealthBar(screen)
        self.drawCurrentTurn(turn,screen)