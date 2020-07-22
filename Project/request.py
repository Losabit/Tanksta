import requests
import json
from online import Online

# https://fr.python-requests.org/en/latest/user/quickstart.html
url = 'http://py.saveyourfood.fr:8000/'


class RequestServer():
    def __init__(self):
        self.player = None

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
        r = requests.put(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player), headers=headers)
        self.player = json.loads(r.text)

    def checkGameIsFind(self):
        if self.player is None:
            return
        r = requests.get(url + "/players/" + str(self.player["id"]) + "/?format=json")
        result = json.loads(r.text)
        if result["play_on"] is not None:
            self.loadGame(result["play_on"])

    def loadGame(self, game_id, tank):
        self.player["health"] = tank
        self.player["pos_x"] = tank.body_rect.x
        self.player["pos_y"] = tank.body_rect.y
        self.player["canon_orientation"] = tank.canon_angle
        r = requests.put(url + '/players/' + str(self.player["id"]), data=self.player)
        players = []
        count = 0
        r = requests.get(url + '/players/' + "/?format=json")
        result = json.loads(r.text)
        for p in result:
            if game_id == p["play_on"]:
                players[count] = p
                count += 1
        Online(650, count, players)

    def delete(self):
        if self.player is None:
            return
        headers = {'Content-type': 'application/json'}
        r = requests.delete(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player), headers=headers)
