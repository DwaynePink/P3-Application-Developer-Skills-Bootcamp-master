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

    def match_following_round(self):
        # Logic to match players for following rounds
        pass

matchmaker = Matchmaking()  # Define the matchmaker instance here

# Add players to the matchmaker
player1 = Player("Player 1", "player1@example.com", "P1", "01-01-2000")
player2 = Player("Player 2", "player2@example.com", "P2", "02-02-2000")
player3 = Player("Player 3", "player3@example.com", "P3", "03-03-2000")
player4 = Player("Player 4", "player4@example.com", "P4", "04-04-2000")
matchmaker.players.extend([player1, player2, player3, player4])

# Call shuffle_players and match_first_round methods
matchmaker.shuffle_players()
matchups, points = matchmaker.match_first_round()

# Print the matchups and points
print("Matchups for the first round:")
for idx, (player1, player2) in enumerate(matchups, 1):
    print(f"Match {idx}: {player1.name} vs {player2.name}")

print("\nInitial points for players:")
for player, point in points.items():
    print(f"{player.name}: {point}")
