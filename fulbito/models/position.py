from typing import List
from pydantic import BaseModel


class TeamPosition(BaseModel):
    """Class representing a team in a position table."""
    position: int
    club: str
    points: int
    games_played: int
    wins: int
    draws: int
    losses: int
    goals_for: int
    goals_against: int
    goals_diff: int

    def __init__(
            self,
            info: List[str]
    ):
        super().__init__(
            position=int(info[0]),
            club=info[1],
            points=int(info[2]),
            games_played=int(info[3]),
            wins=int(info[4]),
            draws=int(info[5]),
            losses=int(info[6]),
            goals_for=int(info[7]),
            goals_against=int(info[8]),
            goals_diff=int(info[9])
        )


class TeamPositionAverage(BaseModel):
    """Class representing a team in an average position table."""
    position: int
    team: str
    year_1_points: int
    year_2_points: int
    year_3_points: int
    total_points: int
    played_games: int
    average_points: float

    def __init__(self, info: List[str]):
        super().__init__(
            position=int(info[0]),
            team=info[1],
            year_1_points=int(info[2]),
            year_2_points=int(info[3]),
            year_3_points=int(info[4]),
            total_points=int(info[5]),
            played_games=int(info[6]),
            average_points=float(info[7])
        )
