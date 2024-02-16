import random
from collections import defaultdict
from models.player import Player
from screens import players


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
        print("Players shuffled successfully.")

    def match_first_round(self):
        """
        Function designed specifically for the first round which is a random shuffle
        """
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

    def update_tournament_results(self, tournament):
        # Retrieve match results from the completed round
        round_results = tournament.get_round_results()

        # Update player data based on match results
        for match_result in round_results:
            winner = match_result['winner']
            loser = match_result['loser']

            # Update player statistics
            winner.increment_wins()
            loser.increment_losses()

    def match_following_round(self, tournament):
        """
        Function designed to match all following rounds. Players are sorted
        by rank, so highest points players are matched but also take into account
        if players have played one another.
        """
        sorted_players = sorted(self.players, key=lambda x: x.points, reverse=True)

        print(f"Number of players available for pairing: {len(sorted_players)}")
        print(len(self.players))

        self.shuffle_players()
        """ Add list to list for matchups """
        matchups = []
        used_pairs = set()
        for i in range(0, len(sorted_players), 2):
            player1 = sorted_players[i]
            player2 = sorted_players[i + 1]

            # Print the players being paired for debugging
            print(f"Pairing: {player1.name} vs {player2.name}")

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

        """" 
        Print the generated matchups for for next round so coordinator can 
        announce next round matchups. 
        """
        print("Generated matchups for the next round:")
        for idx, (player1, player2) in enumerate(matchups, 1):
            print(f"Match {idx}: {player1.name} vs {player2.name}")

        return matchups
