Castle Chess Program
Welcome to the Castle Chess program! This application allows you to manage chess tournaments, clubs, players, and more. Follow the instructions below to set up and run the program on your system.
Setup Instructions
1.	Clone the Repository:
First open attached documents sent. 
- use the attached link to git program and download application file.
- create directory application will be in hosted
Second
- open GitBash and enter the following script into git bash
•	Bashcopy code = Git clone <repository -url>

2.	Navigate to the Project Directory:
Change into the project directory with the following command:
- cd castle-chess

3.	Install Dependencies:
With Python installs in your system. Install the required dependencies using pip command:
- pip install -r requirements.txt

Congratulations your system I set up and ready to run the application

Running the Application
Now that you have completed the setup, you can start the Castle Chess program by running the following command in your terminal:
Make sure you are still in the program directory and type python main.py
You will now be in the main screen of the program. 
Running a tournament
In the main screen you will have the following options
Menu:
1. Create a New Tournament
2. Manage an Existing Tournament
3. List all Ongoing Tournaments
4. Remove a Tournament
5. Exit
Create a New Tournament Type 1. 
•	Enter the name of the new tournament: (Tournament Name)
•	Enter the venue for the tournament: (Venue Name) 
•	Enter the start date (YYYY-MM-DD): (Enter Start Date) Date must be in the format displayed to continue
•	Enter the end date (YYYY-MM-DD): (Enter End Date) Date must be in the format displayed to continue
•	Enter the number of players to select (must be an even number): (Enter Number)
•	Enter a name or chess ID to search, or just press enter to list all players: 
(There are a few different ways you can register a player for the tournament)
-You can click enter and search through the list of players and select the corresponding numbers attached to there name. 
-You can enter a first or last name and select the number that corresponds to that player
-You can enter the players chess id and click the number that corresponds to the name
-If the player doesn’t know their name =) you can enter a partial name or chest id and make sure to select the correct number corresponded to the name of the player. 
•	Enter the maximum number of rounds : 
Congratulations you have successfully create your first tournament! 
And the application will sort, shuffle and pair the players randomly. 
You first round matchup will immediately appear on your screen and you can communicate matchups and let the games begin! 
List all Ongoing Tournament: Type 3. 
•	Anytime you would like to see what current ongoing tournaments are running you can simply select List all Ongoing Tournaments. You will see a list of the current tournament by name. 
Remove Tournament: Type 4. 
•	In the event that a tournament was created by mistake or the tournament is forced to be canceled. You can remove any ongoing tournament. 
•	Select (Remove a Tournament) and select the tournament you would like to remove. 
•	Confirmation will be given “Name Tournament” has been removed.
Now that you have successfully created your new tournaments you will move to the manage existing tournaments screen. 
Manage an Existing Tournament: Type 2
•	You will see a list of current tournaments simply select the one you wish to manage. 
•	Your Tournament will be selected and details will be printed including the name, venue, players, dates of the tournament and current round the tournament is in. 
From here you will have several options to choose from. 
Menu:
1. View Rankings
2. View Matchups
3. Play Next Round
4. View Player Details
5. Print Tournament Reports
View Rankings: Type 1 for player rankings
View Matchups: Type 2 for Tournament Matchups
Play Next Round: Type 3
•	You will be prompted to confirm you would like to advance to the next round. Type yes
•	Each match up will be listed and simply add 1 for the winner or 0 for a draw
•	Once complete next round matchups will print for your view. The previous round results will displayed and automatically saved as a JSON file.
•	Continue to play next round until system concludes and winner is declared. Ty
View Player Details: Type 4 
•	Play Details will be displayed. 
Print Tournament Report: Type 5
•	You will list of players, matches and as well results for the tournament. 
Back to Main Menu: Type 6
Generating the Flake8 Report
A Flake 8 file has been added to the source file. To generate a new Flake8 Report simply. 
Change directory into the project folder-     	Terminal Command: 	cd (name of file)  
Activate the virtual Environment- 		Terminal Command: 	.\env\Scripts\activate
Run Flake8 Report-			Terminal Command: 	flake8 --max-line-length=119 --exclude env --format=html --htmldir=flake-report 
Contributions
Contributions to the Castle Chess program are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.
________________________________________
Feel free to customize and expand this README with additional details specific to your Castle Chess program. Let me know if you need further assistance!
