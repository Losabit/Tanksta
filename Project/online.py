import sys
import pygame

sys.path.append('controllers')
from controllers.player import Player
from tank import Tank

MOVEMENT_LIMIT = 120


class Online():
    numberOfPlayers = 0

    def __init__(self, server):
        if len(server.players) == 0:
            print("need more than 1 player")
            pygame.quit()
        print(server.players)
        self.server = server
        self.tanks = self.initTankPositions(server.players)
        self.player_tank = Tank(tuple([server.player['pos_x'], server.player['pos_y']]))
        self.player_tank.canon_angle = server.player['canon_orientation']
        self.player = Player(self.player_tank)

    def initTankPositions(self, players):
        tanks = []
        for player in players:
            tanks.append(Tank(tuple([player['pos_x'], player['pos_y']])))
            tanks[len(tanks) - 1].canon_angle = player['canon_orientation']
        return tanks

    def update(self, screen):
        if self.server.current_player == None:
            print("errooooor")
        if self.server.current_player['id'] == self.server.player['id']:
            self.server.sendInfo()
            for event in pygame.event.get():
                self.player.controller(event)
                if event.type == pygame.QUIT:
                    self.server.delete()
                    pygame.quit()
                    print("Game Closed")
        else:
            self.server.getInfo()
           

            

        for tank in self.tanks:
            tank.display(screen, self.tanks)
        self.player.tank.display(screen, self.tanks)
        '''
        for i in range(len(self.tanks)):
            if i >= len(self.tanks):
                i = len(self.tanks) - 1
            if self.tanks[i].health <= 0:
                del self.tanks[i]

        if len(self.tanks) == 1:
            return False
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.server.delete()
                pygame.quit()
                print("Game Closed")

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
