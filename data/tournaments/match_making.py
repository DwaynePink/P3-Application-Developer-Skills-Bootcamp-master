import random
from collections import defaultdict


class Matchmaking:
    """
    Class is responsible for all matchmaking as well as updating player points and
    tournament results, which are both needed for the matchmaking process
    """
    def __init__(self, players=None):
        self.players = players if players is not None else []

    def shuffle_players(self):
        """
        Shuffle players is used for first round match up as well as after logic
        for match making in the following rounds.
        """
        if len(self.players) % 2 != 0:
            raise ValueError("Number of players must be even for matchmaking.")
        random.shuffle(self.players)
        print("Tournament created.")
        print("Players shuffled.")

    def match_first_round(self, players):
        """
        Function designed specifically for the first round which is a random shuffle, iterates
        over the shuffled list and match pairs. initializes points for each player.
        """
        if len(players) < 2:
            raise ValueError("At least two players are required for matchmaking.")

        self.shuffle_players()
        matchups = []
        points = defaultdict(float)

        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            matchups.append((player1, player2))
            points[player1] = 0
            points[player2] = 0

        return matchups, points

    def match_following_round(self, tournament):
        """
        Function designed to match all following rounds. Players are sorted by rank, so
        that players wth the highest points are matched first, then shuffles the list and
        iterates over shuffled list to avoid pairing players whom have been paired before.
        """
        sorted_players = sorted(tournament.players, key=lambda x: x.points, reverse=True)

        self.shuffle_players()
        """ Add list to list for matchups """
        matchups = []
        used_pairs = set()
        for i in range(0, len(sorted_players), 2):
            player1 = sorted_players[i]
            player2 = sorted_players[i + 1]

            """
            Check if pair has already played against each other
            """
            pair = tuple(sorted([player1, player2]))
            while pair in used_pairs:
                # Add debug statements to understand the flow
                print("Repeating pair found. Re-generating matchups...")
                print(f"Current pair: {pair}")
                print("Current used pairs:", used_pairs)

                """
                Generate Pairs for the next rounds
                """
                player1, player2 = random.sample(sorted_players, 2)
                pair = tuple(sorted([player1, player2]))

                print(f"New pair: {pair}")

            used_pairs.add(pair)
            matchups.append((player1, player2))

        """
        Print the generated matchups for for next round so coordinator can
        announce next round matchups.
        """
        print("Generated matchups for the next round:")
        for idx, (player1, player2) in enumerate(matchups, 1):
            print(f"Match {idx}: {player1.name} vs {player2.name}")

        return matchups
