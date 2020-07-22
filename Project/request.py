import pygame
import requests
import json

from pygame import font
import pygame_gui
from utils.timeCapsule import TimeCapsule

from online import Online

# https://fr.python-requests.org/en/latest/user/quickstart.html
url = 'http://py.saveyourfood.fr:8000/'


class RequestServer():
    def __init__(self):
        self.player = None
        self.game = None
        self.players = []
        self.current_player = None

    def playOnline(self):
        payload = {'pseudo': 'losabit', 'want_to_play': False}
        headers = {'Content-type': 'application/json'}
        r = requests.post(url + '/players/?format=json', data=json.dumps(payload), headers=headers)
        self.player = json.loads(r.text)

    def wantToPlay(self):
        if self.player is None:
            return
        self.player['want_to_play'] = True
        headers = {'Content-type': 'application/json'}
        r = requests.put(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player),
                         headers=headers)
        self.player = json.loads(r.text)

    def checkGameIsFind(self):
        if self.player is None:
            return
        r = requests.get(url + "/players/" + str(self.player["id"]) + "?format=json")
        result = json.loads(r.text)
        if result["play_on"] is not None:
            self.player = result
            r = requests.get(url + "/games/" + str(result["play_on"]) + "?format=json")
            self.game = json.loads(r.text)
            if self.game["turn_id"] is not None:
                self.getInfo()
                return True
            else:
                return False
        else:
            return False

    def loadGame(self):
        r = requests.get(url + '/players/?format=json')
        result = json.loads(r.text)
        for player in result:
            if player['play_on'] == self.game['id'] and player['id'] != self.player['id']:
                self.players.append(player)
        r = requests.get(url + "/players/" + str(self.player["id"]) + "?format=json")
        self.player = json.loads(r.text)

    def endTurn(self):
        if self.player is None:
            return
        self.player['end_of_turn'] = True
        headers = {'Content-type': 'application/json'}
        r = requests.put(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player), headers=headers)
        self.player = json.loads(r.text)
        self.getInfo()
        
    def getInfo(self):
        r = requests.get(url + "/games/" + str(self.game["id"]) + "?format=json")
        self.game = json.loads(r.text)
        r = requests.get(url + "/players/" + str(self.game["turn_id"]) + "?format=json")
        self.current_player = json.loads(r.text)

    def sendInfo(self, tank):
        headers = {'Content-type': 'application/json'}
        self.player['pos_x'] = tank.body_rect.x
        self.player['pos_y'] = tank.body_rect.y
        self.player['shoot'] = len(tank.bullets) >= 1
        if self.player['shoot']:
            self.player['puissance'] = tank.bullets[0].puissance
        self.player['canon_orientation'] = tank.canon_angle

        r = requests.put(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player), headers=headers)
        self.player = json.loads(r.text)

    def getNbValidate(self, online_manager):
        initt = 5
        if self.game["players"] >= self.game["players_want_play"]:
            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render("{1} on {0} as validate".format(self.game["players"], self.game["players_want_play"]),
                               True, (120, 0, 0))
            label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((900, 400), (200, 200)),text="{1} on {0} as "
                                                                                                      "validate".format(self.game["players"], self.game["players_want_play"]),manager=online_manager)
            #print("{1} on {0} as validate".format(self.game["players"], self.game["players_want_play"]))
            t = TimeCapsule(initt)

    def delete(self):
        if self.player is None:
            return
        headers = {'Content-type': 'application/json'}
        r = requests.delete(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player),
                            headers=headers)
