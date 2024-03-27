from typing import List
from pydantic import BaseModel

from position import TeamPosition, TeamPositionAverage
from top import TopScorers, TopAssists


class CopaLigaData(BaseModel):
    """Class that contains all Copa de la liga's information."""
    group_a: List[TeamPosition]
    group_b: List[TeamPosition]
    annual_standings: List[TeamPosition]
    average_standings: List[TeamPositionAverage]
    top_scorers: List[TopScorers]
    top_assists: List[TopAssists]

    def __init__(
            self,
            group_a: List[TeamPosition],
            group_b: List[TeamPosition],
            annual_standings: List[TeamPosition],
            top_scorers: List[TopScorers],
            top_assists: List[TopAssists],
            average_standings: List[TeamPositionAverage]
    ):
        super().__init__(
            group_a=group_a,
            group_b=group_b,
            annual_standings=annual_standings,
            top_scorers=top_scorers,
            top_assists=top_assists,
            average_standings=average_standings
        )


class LigaArgData(BaseModel):
    """Class that contains all Liga Argentina information."""
    standings: List[TeamPosition]
    annual_standings: List[TeamPosition]
    average_standings: List[TeamPositionAverage]
    top_scorers: List[TopScorers]
    top_assists: List[TopAssists]

    def __init__(
            self,
            standings: List[TeamPosition],
            annual_standings: List[TeamPosition],
            average_standings: List[TeamPositionAverage],
            top_scorers: List[TopScorers],
            top_assists: List[TopAssists]
    ):
        super().__init__(
            standings=standings,
            annual_standings=annual_standings,
            average_standings=average_standings,
            top_scorers=top_scorers,
            top_assists=top_assists
        )


class EuropeanLeagueData(BaseModel):
    """Class that contains all a European League information."""
    standings: List[TeamPosition]
    top_scorers: List[TopScorers]
    top_assists: List[TopAssists]

    def __init__(
            self,
            standings: List[TeamPosition],
            top_scorers: List[TopScorers],
            top_assists: List[TopAssists]
    ):
        super().__init__(
            standings=standings,
            top_scorers=top_scorers,
            top_assists=top_assists
        )
