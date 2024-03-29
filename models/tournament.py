from .round import Round
from data.tournaments.match_making import Matchmaking


class Tournament:
    players = None
    """
    Intended to store  player information shared among tournament class.
    parameter are displayed below.
    """
    def __init__(self, name, venue, start_date, end_date, players, max_round):
        if not name:
            raise ValueError("Player name is required!")

        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.max_round = max_round
        self.rounds = []
        self.current_round = 0
        self.is_round_setup_done = False
        self.matchmaking = Matchmaking()

    def sort_players(self):
        # Sort players based on their points in descending order
        self.players.sort(key=lambda player: player.points, reverse=True)

    def play_round(self):
        """
        Handles round setup. Check if maximum number of rounds is reached. if max rounds are
        not reached proceed to set up current round. Creates list of named 'rounds' to store
        for matchups. After round is set up, it returns to prepare for next round setup.
        """
        if self.current_round >= self.max_round:
            print("Maximum number of rounds reached. No new rounds will occur")
            return False

        if not self.is_round_setup_done:
            self.current_round += 1
            self.is_round_setup_done = True

            if not self.rounds:
                pass

            else:
                self.sort_players()

            rounds = []
            # Make rounds
            for i in range(0, len(self.players), 2):
                if i + 1 < len(self.players):
                    round = Round(self.players[i], self.players[i + 1])
                    rounds.append(round)

            self.rounds.append(rounds)

        self.is_round_setup_done = False
        return True

    def display_player_info(self):
        for player in sorted(self.players, key=lambda p: p.points, reverse=True):
            print(player)

    def display_rankings(self):
        sorted_players = sorted(self.players, key=lambda x: x.points, reverse=True)
        for player in sorted_players:
            print(f"Name: {player.name}, Points: {player.points}")
