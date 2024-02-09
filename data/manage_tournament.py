import os
import json
import random
from data.match_making import Matchmaking
from models.tournament import Tournament
from models.player import Player
from thefuzz import process

class ManageTournament:
    def __init__(self):
        self.tournaments = {}
        self.all_players = []
        self.load_all_clubs()
        self.matchmaker = Matchmaking()

    def load_all_clubs(self):
        base_path = r"\Users\dwayn\PycharmProjects\P3-Application-Developer-Skills-Bootcamp-Dwayne\data\clubs"
        club_files = ["cornville.json", "springfield.json"]
        for club_file in club_files:
            club_name, club_players = self.load_club(os.path.join(base_path, club_file))
            self.all_players.extend(club_players)

    def load_club(self, file_path):
        # Reads player data from a club file and returns the club's name and its players.
        with open(file_path, 'r') as file:
            data = json.load(file)
            players = [Player(player['name'], player['email'], player['chess_id'], player['birthday'])
                       for player in data['players']]
            return data["name"], players

    def create_tournament(self):
        # Creates a new tournament based on user input.
        # Handles tournament creation including venue, dates, player selection, and max rounds.
        tournament_name = input("Enter the name of the new tournament: ").strip()
        venue = input("Enter the venue for the tournament: ").strip()
        start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter the end date (YYYY-MM-DD): ").strip()

        if tournament_name in self.tournaments:
            print(f"Tournament '{tournament_name}' already exists.")
            return

        num_players = 0
        while True:
            try:
                num_players = int(input("Enter the number of players to select (must be an even number): "))
                if num_players % 2 == 0 and num_players > 0:
                    break  # break out of the loop if input is valid
                else:
                    print("Invalid number. Please enter a positive even number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        selected_players = self.select_players(num_players)

        max_rounds = int(input("Enter the maximum number of rounds: "))

        # Create and add tournament to the list of tournaments
        new_tournament = Tournament(tournament_name, venue, start_date, end_date, selected_players, max_rounds)
        self.tournaments[tournament_name] = new_tournament

        # Initialize matchmaker and start matchmaking process
        self.matchmaker = Matchmaking()
        self.matchmaker.players.extend(selected_players)  # Add selected players to the matchmaker
        self.matchmaker.shuffle_players()  # Shuffle players
        matchups, _ = self.matchmaker.match_first_round()  # Match the first round

        print("Tournament created successfully.")
        print("Matchups for the first round:")
        for idx, (player1, player2) in enumerate(matchups, 1):
            print(f"Match {idx}: {player1.name} vs {player2.name}")

    def calculate_first_round_matchups(self, tournament):
        random.shuffle(tournament.players)
        num_players = len(tournament.players)
        for i in range(0, num_players, 2):
            player1 = tournament.players[i]
            player2 = tournament.players[i + 1]
            tournament.rounds[0].append(Match(player1, player2))

        print("Match-ups for the first round:")
        for i, match in enumerate(tournament.rounds[0], start=1):
            print(f"Match {i}: {match.player1.name} vs {match.player2.name}")

    def play_next_round(self, tournament):
        # Handles the gameplay for the next round in the given tournament.
        # Processes match results based on user input.
        # first checks if max rounds have been reached
        if tournament.current_round >= tournament.max_round:
            print("Maximum number of rounds reached. No new rounds will occur")
            return False

        print(f"Attempting to play round {tournament.current_round + 1}.\n"
              f"Current round: {tournament.current_round}\n"
              f"Max rounds: {tournament.max_round}")
        # If it's the first round, calculate match-ups

        if tournament.current_round == 0:
            # print added for debugging will be removed after
            print("Calculating match-ups for the first round.")
            self.calculate_first_round_matchups(tournament)

        if tournament.current_round >= tournament.max_round:
            print("Maximum number of rounds reached. The tournament has concluded.")
            self.declare_winner(tournament)
            return

        if not tournament.play_round():
            return

        current_round = tournament.rounds[tournament.current_round - 1]
        for i, match in enumerate(current_round, start=1):
            if not match.is_played():
                print(f"Match {i}: {match.player1.name} vs {match.player2.name}")
                while True:
                    result = input("Enter winner (1 for player1, 2 for player2, 0 for draw): ").strip()
                    if result in ["1", "2", "0"]:
                        if result == "1":
                            match.play_match("player1")
                        elif result == "2":
                            match.play_match("player2")
                        else:
                            match.play_match("draw")
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 0.")

        print(f"After Round {tournament.current_round}:")
        self.save_tournament_state(tournament, tournament.current_round)
        tournament.display_rankings()

        if tournament.current_round == tournament.max_round:
            print("Maximum number of rounds reached. The tournament has concluded.")
            self.declare_winner(tournament)

    def view_player_details(self, tournament_name):
        # Displays details of all players participating in a specific tournament.
        tournament = self.tournaments.get(tournament_name)
        if not tournament:
            print(f"No tournament found with the name '{tournament_name}'.")
            return

        print(f"Player details for {tournament.name}:")
        for player in tournament.players:
            print(f" - {player.name}, Chess ID: {player.chess_id})")
    def search_players(self, search_term):
        # Searches and returns players matching the given search term (name or chess ID).
        return [player for player in self.all_players
                if search_term.lower() in player.name.lower()
                or search_term.lower() in player.chess_id.lower()
                or search_term.lower() in player.name.lower().split()]
    def select_players(self, num_players):
        # Selects players for a tournament based on user input.
        selected_players = []

        while len(selected_players) < num_players:
            while True:
                try:
                    search_term = input("Enter a name or chess ID to search, or just press enter to list all players: ")
                    display_list = self.search_players(search_term) if search_term else self.all_players

                    for i, player in enumerate(display_list, 1):
                        print(f"{i}: {player.name} ({player.chess_id})")

                    player_index = int(input(f"Select player {len(selected_players) + 1} (enter number): ")) - 1
                    if 0 <= player_index < len(display_list):
                        selected_player = display_list[player_index]
                        if selected_player not in selected_players:
                            selected_players.append(selected_player)
                            self.display_selected_players(selected_players)
                            break  # break out of the inner loop if input is valid
                        else:
                            print("Player already selected. Please choose a different player.")
                    else:
                        print("Invalid player number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        return selected_players

    def display_selected_players(self, selected_players):
        # Displays a list of currently selected players for the tournament.
        print("\nCurrently selected players:")
        for i, player in enumerate(selected_players, 1):
            print(f"{i}: {player.name} ({player.chess_id})")
        print()

    def print_tournament_report(self, tournament):
        # Prints a detailed report of the tournament including players, rounds, and matches.
        print(f"\nTournament Report for: {tournament.name}")
        print(f"Dates: {tournament.start_date} to {tournament.end_date}")
        print(f"Venue: {tournament.venue}")
        print(f"Current Round: {tournament.current_round}/{tournament.max_round}")

        print("\nPlayers (sorted by points):")
        sorted_players = sorted(tournament.players, key=lambda x: x.points, reverse=True)
        for player in sorted_players:
            print(f" - {player.name} (Points: {player.points})")

        print("\nRounds and Matches:")
        for round_num, round_matches in enumerate(tournament.rounds, start=1):
            print(f"Round {round_num}:")
            for match in round_matches:
                match_info = f"{match.player1.name} vs {match.player2.name}"
                if match.played:
                    result = f"Result: {match.result}"
                else:
                    result = "Not played yet"
                print(f" - Match: {match_info}, {result}")

    def list_tournaments(self):
        # Lists all ongoing tournaments.
        if not self.tournaments:
            print("There are no ongoing tournaments.")
            return

        print("Ongoing Tournaments:")
        for tournament_name in self.tournaments.keys():
            print(tournament_name)

    def remove_tournament(self):
        # Removes a tournament from the tournaments list based on user input.
        if not self.tournaments:
            print("There are no ongoing tournaments to remove.")
            return

        tournament_name = input("Enter the name of the tournament to remove: ").strip()
        if tournament_name in self.tournaments:
            del self.tournaments[tournament_name]
            print(f"Tournament '{tournament_name}' has been removed.")
        else:
            print(f"No tournament found with the name '{tournament_name}'.")

    def search_players_objects(self, search_term):
        # Searches and returns player objects matching the given search term (name or chess ID).
        matched_players = []
        for player in self.all_players:
            # Check for exact match in name or chess ID
            if (search_term.lower() in player.name.lower()) or (search_term.lower() in player.chess_id.lower()):
                matched_players.append(player)
            else:
                # Perform fuzzy matching
                matches = process.extract(search_term.lower(), player.name.lower(), scorer=process.partial_ratio)
                for _, score in matches:
                    if score > 50:  # Adjust the threshold as needed
                        matched_players.append(player)
                        break  # Break loop if a match is found
        return matched_players

    def save_tournament_state(self, tournament, round_number):
        # Saves the state of the current round of the tournament to a JSON file.
        round_data = []
        for match in tournament.rounds[round_number - 1]:
            player1_info = f"{match.player1.name} (ID: {match.player1.chess_id})"
            player2_info = f"{match.player2.name} (ID: {match.player2.chess_id})"

            if match.result == "player1":
                winner_info = player1_info
            elif match.result == "player2":
                winner_info = player2_info
            else:
                winner_info = 'draw'

            match_info = {
                'player1': player1_info,
                'player2': player2_info,
                'winner': winner_info
            }
            round_data.append(match_info)

        file_name = f"{tournament.name}_round_{round_number}.json"
        try:
            file_path = file_name

            with open(file_path, 'w') as file:
                json.dump(round_data, file, indent=4)

            print(f"Round {round_number} data saved in {os.path.abspath(file_path)}")
        except Exception as e:
            print(f"Failed to save tournament state: {e}")
