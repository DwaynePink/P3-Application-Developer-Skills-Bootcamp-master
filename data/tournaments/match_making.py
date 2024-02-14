import random
from collections import defaultdict
from models.player import Player
from screens import players


class Matchmaking:
    def __init__(self, players=None):
        self.players = players if players is not None else []


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

    def match_following_round(self, previous_round_results):
        # Sort players by their points (descending order)
        sorted_players = sorted(self.players, key=lambda x: x.points, reverse=True)

        # Print the number of players available for pairing
        print(f"Number of players available for pairing: {len(sorted_players)}")
        print(len(self.players))
        # Pair players for the next round

        matchups = []
        used_pairs = set()
        for i in range(0, len(sorted_players), 2):
            player1 = sorted_players[i]
            player2 = sorted_players[i + 1]

            # Print the players being paired for debugging
            print(f"Pairing: {player1.name} vs {player2.name}")

            # Check if this pair has already played against each other
            pair = tuple(sorted([player1, player2]))
            while pair in used_pairs:
                # Add debug statements to understand the flow
                print("Repeating pair found. Re-generating matchups...")
                print(f"Current pair: {pair}")
                print("Current used pairs:", used_pairs)

                #Generate a new pair
                player1, player2 = random.sample(sorted_players, 2)
                pair = tuple(sorted([player1, player2]))

                print(f"New pair: {pair}")

            used_pairs.add(pair)
            matchups.append((player1, player2))

        # Print the generated matchups for inspection
        print("Generated matchups for the next round:")
        for idx, (player1, player2) in enumerate(matchups, 1):
            print(f"Match {idx}: {player1.name} vs {player2.name}")

        return matchups

"""
    }
    matchmaking = Matchmaking(players)
    # Match the following round
    matchups = matchmaking.match_following_round(previous_round_results)
    for idx, (player1, player2) in enumerate(matchups, 1):
        print(f"Match {idx}: {player1.name} vs {player2.name}")
"""