from data.tournaments.manage_tournament import ManageTournament
from screens.tournaments.view import TournamentView


def main():
    """
    This is the entry point to the system. Give users options to manage or create tournaments.
    Enters loop when user makes a selection and exits when user chooses to exit.
    """
    manager = ManageTournament()
    tview = TournamentView(manager)

    while True:
        print("\nMenu:")
        print("1. Create a New Tournament")
        print("2. Manage an Existing Tournament")
        print("3. List all Ongoing Tournaments")
        print("4. Remove a Tournament")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manager.create_tournament()
        elif choice == '2':
            tview.manage_tournament()
        elif choice == '3':
            manager.list_tournaments()
        elif choice == '4':
            manager.remove_tournament()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()