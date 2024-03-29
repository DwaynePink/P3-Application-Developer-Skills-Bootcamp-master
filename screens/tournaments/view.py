from data.tournaments.Report_manager import TournamentReporter
from models import tournament


class TournamentView:
    """
    Class Responsible for managing the user interface for managing tournaments.
    Tournament_manager manages the backend logic for tournaments.
    """
    def __init__(self, tournament_manager):
        self.tournament_manager = tournament_manager
        self.tournament_reports = TournamentReporter(tournament)

    def manage_tournament(self):
        """
        Method to manage a tournament. It includes listing available
        tournaments,selecting a tournament, and managing various aspects
        of the selected tournament.
        """
        if not self.tournament_manager.tournaments:
            print("No tournaments available.")
            return

        print("\nAvailable Tournaments:")
        """
        Retrieve and display the list of available tournament names
        """
        tournament_names = list(self.tournament_manager.tournaments.keys())
        for i, name in enumerate(tournament_names, 1):
            print(f"{i}. {name}")

        """
        Prompts the user to select a tournament to manage
        """
        choice = input("Select a tournament to manage (enter number): ").strip()
        try:
            choice_index = int(choice) - 1
            # Validate the user's selection and retrieve the corresponding tournament
            if 0 <= choice_index < len(tournament_names):
                tournament_name = tournament_names[choice_index]
                tournament = self.tournament_manager.tournaments[tournament_name]
            else:
                print("Invalid selection. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        """
        Main loop for managing the selected tournament with various options.
        """
        while True:
            print(f"\nManaging Tournament: {tournament.name}")
            # Display details of the selected tournament
            print(f"Venue: {tournament.venue}")
            print(f"Dates: {tournament.start_date} to {tournament.end_date}")
            print(f"Current Round: {tournament.current_round} / {tournament.max_round}")
            print("Players:")
            # List all players in the tournament
            for player in tournament.players:
                print(f" - {player.name} (Points: {player.points})")

            """
            Menu for tournament management options
            """
            print("1. View Rankings")
            print("2. Play Next Round")
            print("3. View Player Details")
            print("4. Print Tournament Report")
            print("5. Back to Main Menu")
            choice = input("Choose an option: ")

            """
            Handles the user's choice for tournament management.
            """
            if choice == '1':
                tournament.display_rankings()
            elif choice == '2':
                self.tournament_manager.play_next_round(tournament)
            elif choice == '3':
                self.tournament_manager.view_player_details(tournament.name)
            elif choice == '4':
                reporter = TournamentReporter(tournament)
                reporter.print_tournament_report()
            elif choice == '5':
                break
            else:
                print("Invalid option, please try again.")
