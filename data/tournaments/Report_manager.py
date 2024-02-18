from models import tournament


class TournamentReporter:
    """
    Provides reporting functionality related to tournaments. constructor takes tournament
    parameter allowing other methods within the class to access info about the tournament.
    """
    def __init__(self, tournament):
        self.tournament = tournament

    def print_tournament_report(self):
        """
        Prints necessary tournament information including name, date, venue, current rounds.
        Displays player rankings and prints matchups for each round.
        """
        print(f"\nTournament Report for: {self.tournament.name}")
        print(f"Dates: {self.tournament.start_date} to {self.tournament.end_date}")
        print(f"Venue: {self.tournament.venue}")
        print(f"Current Round: {self.tournament.current_round}/{self.tournament.max_round}")

        print("\nPlayers (sorted by points):")
        sorted_players = sorted(self.tournament.players, key=lambda x: x.points, reverse=True)
        for player in sorted_players:
            print(f" - {player.name} (Points: {player.points})")

        print("\nRounds and Matches:")
        for round_num, round_matches in enumerate(self.tournament.rounds, start=1):
            print(f"Round {round_num}:")
            for match in round_matches:
                match_info = f"{match.player1.name} vs {match.player2.name}"
                if match.played:
                    if match.result == "player1":
                        winner_name = match.player1.name
                    elif match.result == "player2":
                        winner_name = match.player2.name
                    else:
                        winner_name = "Draw"
                    result = f"Result: {winner_name}"
                else:
                    result = "Not played yet"
                print(f" - Match: {match_info}, {result}")
