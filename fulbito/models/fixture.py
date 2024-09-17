from dataclasses import dataclass
from typing import List

@dataclass
class Fixture:
    date: str
    matches: List[List[str]]  # List of matches, where each match is a list of strings

    def __init__(self, matches_data: List[List[str]]):
        if matches_data:
            self.date = matches_data[0][0]  # The first element is the date
            self.matches = matches_data  # Store the matches data
        else:
            self.date = ""
            self.matches = []