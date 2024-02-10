import random
from collections import defaultdict
from models.player import Player


class Matchmaking:
    def __init__(self):
        self.players = []



        def match_following_round(self, previous_round_results):
            # Sort players by their points (descending order)
            sorted_players = sorted(self.players, key=lambda x: x.points, reverse=True)

            # Pair players for the next round
            matchups = []
            used_pairs = set()
            for i in range(0, len(sorted_players), 2):
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1]

                # Check if this pair has already played against each other
                pair = tuple(sorted([player1, player2]))
                while pair in used_pairs:
                    player1, player2 = random.sample(sorted_players, 2)
                    pair = tuple(sorted([player1, player2]))

                used_pairs.add(pair)
                matchups.append((player1, player2))

            print("Round matchups created successfully.")
            return matchups

    # Example usage
    players = [Player("Player 1", 1), Player("Player 2", 0), Player("Player 3", 2), Player("Player 4", 1)]
    matchmaking = Matchmaking(players)

    # Simulate previous round results (for demonstration)
    previous_round_results = {
        ("Player 1", "Player 3"): "Player 3 wins",
        ("Player 2", "Player 4"): "Player 4 wins"
    }

    # Match the following round
    matchups = matchmaking.match_following_round(previous_round_results)
    for idx, (player1, player2) in enumerate(matchups, 1):
        print(f"Match {idx}: {player1.name} vs {player2.name}")

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
