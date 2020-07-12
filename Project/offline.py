import sys
import pygame

sys.path.append('controllers')
from player import Player
from ai import AI
from tank import Tank

MOVEMENT_LIMIT = 120

class Offline():
    def __init__(self, numberOfPlayers, y):
        self.tanks = self.initTankPositions(numberOfPlayers, y)
        self.player = Player(self.tanks[0])
        self.ai = [AI(self.tanks[i]) for i in range(1, len(self.tanks))]
        self.turn = -1
        self.origin_tank_position = None
        self.nextTurn()
        

    def initTankPositions(self, numberOfTank, y):
        tanks = []
        for i in range(numberOfTank):
            tanks.append(Tank(tuple([350 + i * 400, y])))
        return tanks

    def update(self, screen):
        if self.turn == 0:
            self.player.update()
            if self.difference_position(self.origin_tank_position, self.player.tank.body_rect) > MOVEMENT_LIMIT or len(self.player.tank.bullets) >= 1:
                self.nextTurn()
                self.player.stop()
        else:
            self.ai[self.turn - 1].random_controller(None)
            if self.difference_position(self.origin_tank_position, self.ai[self.turn - 1].tank.body_rect) > MOVEMENT_LIMIT or len(self.ai[self.turn - 1].tank.bullets) >= 1:
                self.nextTurn()
        

        for tank in self.tanks:
            tank.display(screen, self.tanks)
       
        for i in range(len(self.tanks)):
            if i >= len(self.tanks):
                i = len(self.tanks) - 1
            if self.tanks[i].health <= 0:
                del self.tanks[i] 

        if len(self.tanks) == 1:
            return False

        for event in pygame.event.get():
            if self.turn == 0:
                self.player.controller(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Game Closed")
                running = False

        return True

    def difference_position(self, pos1, pos2):
        return abs(pos1[0] - pos2.x) + abs(pos1[1] - pos2.y)

    def nextTurn(self):
        self.turn += 1
        if self.turn == len(self.tanks):
            self.turn = 0

        if self.turn == 0:
            self.origin_tank_position = [self.player.tank.body_rect.x, self.player.tank.body_rect.y]
        else:
            self.origin_tank_position = self.ai[self.turn - 1].tank.body_rect