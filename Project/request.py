import requests
import json
from online import Online

# https://fr.python-requests.org/en/latest/user/quickstart.html
url = 'http://py.saveyourfood.fr:8000/'


class RequestServer():
    def __init__(self):
        self.player = None
        self.game = None

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
        r = requests.get(url + "/players/" + str(self.player["id"]) + "?format=json")
        result = json.loads(r.text)
        if result["play_on"] is not None:
            self.player = result
            r = requests.get(url + "/games/" + str(result["play_on"]) + "?format=json")
            self.game = json.loads(r.text)
            print(self.game)
            return True
        else:
            return False

    def loadGame(self):
        r = requests.get(url + '/players/?format=json')
        result = json.loads(r.text)
        players = []
        count = 0
        r = requests.get(url + '/players/' + "/?format=json")
        result = json.loads(r.text)
        for p in result:
            if game_id == p["play_on"]:
                players[count] = p
                count += 1
        Online(650, count, players)


    def getNbValidate(self, players, game_id):
        r = requests.get(url + '/players/'+"/?format=json")
        resultat = json.loads(r.text)
        for p in resultat:
            print("ok")
        return
    def delete(self):
        if self.player is None:
            return
        headers = {'Content-type': 'application/json'}
        r = requests.delete(url + '/players/' + str(self.player["id"]) + "?format=json", data=json.dumps(self.player), headers=headers)
