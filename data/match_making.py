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

    """
    def match_first_round(self):
        if len(self.players) < 2:
            raise ValueError("At least two players are required for matchmaking.")

        self.shuffle_players()
        matchups = []
        points = defaultdict(float)

        for i in range(0, len(self.players), 2):
            player1 = self.players[i]
            player2 = self.players[i + 1]
            matchups.append((player1, player2))
            points[player1] = 0
            points[player2] = 0

        print("First round matchups created successfully.")
        return matchups, points
    """

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
