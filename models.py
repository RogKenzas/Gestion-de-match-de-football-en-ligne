import json
import os

PLAYERS_FILE = os.path.join('data', 'players.json')
MATCHES_FILE = os.path.join('data', 'matches.json')

def load_players():
    with open(PLAYERS_FILE, 'r') as f:
        return json.load(f)

def save_players(players):
    with open(PLAYERS_FILE, 'w') as f:
        json.dump(players, f, indent=4)

def load_matches():
    with open(MATCHES_FILE, 'r') as f:
        return json.load(f)

def save_matches(matches):
    with open(MATCHES_FILE, 'w') as f:
        json.dump(matches, f, indent=4)
