from typing import List
from pydantic import BaseModel


class TopScorers(BaseModel):
    """Class that contains info of a top scorer."""
    position: int
    team: str
    player_name: str
    goals: int
    penalties: int

    def __init__(self, info: List[str], position: int):
        name_team = info[0].split("(")
        super().__init__(
            player_name=name_team[0][1:-1],
            team=name_team[1][:-1],
            goals=int(info[1]),
            penalties=int(info[2][2:-2]),
            position=position
        )


class TopAssists(BaseModel):
    """Class that contains info of a top assist."""
    position: int
    team: str
    player_name: str
    assists: int

    def __init__(self, info: List[str], position: int):
        name_team = info[0].split("(")
        super().__init__(
            player_name=name_team[0][:-1],
            team=name_team[1][:-1],
            assists=int(info[1]),
            position=position
        )
