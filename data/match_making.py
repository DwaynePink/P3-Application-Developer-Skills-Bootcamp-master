import random
from collections import defaultdict
from models.player import Player


class Matchmaking:
    def __init__(self):
        self.players = []

    def shuffle_players(self):
        if len(self.players) % 2 != 0:
            raise ValueError("Number of players must be even for matchmaking.")
        random.shuffle(self.players)
        print("Players shuffled successfully.")

    def match_following_round(self):
        # Logic to match players for following rounds
        pass

    def update_player_points(self, rounds):
        for rnd in rounds:
            if rnd.was_played():
                if rnd.result == "Draw":
                    rnd.player1.add_points(0.5)
                    rnd.player2.add_points(0.5)
                elif rnd.result == "player1":
                    rnd.player1.add_points(1)
                elif rnd.result == "player2":
                    rnd.player2.add_points(1)
