import pygame
import pygame_gui
from tank import Tank

class GUI():
    def __init__(self,Tanks,manager):
        self.tanks =  Tanks
        self.manager = manager
        self.initHealthBar()

    def initHealthBar(self):
        inc = 0 
        for tank in self.tanks:
            pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect(((1600 / len(self.tanks))*inc, 100), (1600 / len(self.tanks), 50)),manager=self.manager,sprite_to_monitor=tank)
            inc += 1
            
    def drawCurrentTurn(self,turn,screen):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        # now print the text
        text_surface = font.render(f'Playing: Tank {str(turn+1)}' , True, pygame.Color('black'))
        text_rect = text_surface.get_rect(center=(1600/2, 50))
        screen.blit(text_surface, text_rect)

    def draw(self,turn,screen):
        self.drawCurrentTurn(turn,screen)