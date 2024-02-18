import json
from pathlib import Path

from .club import ChessClub


class ClubManager:
    """
    Designed to manage chess clubs. iterates over all files in the
    specified folder, creates a ChessClub object for each file and
    stores them in a JSON file.
    """
    def __init__(self, data_folder="data/clubs"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.clubs = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.clubs.append(ChessClub(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        club = ChessClub(name=name, filepath=filepath)
        club.save()

        self.clubs.append(club)
        return club
