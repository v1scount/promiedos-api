import requests
from typing import List, Type
from bs4 import BeautifulSoup, ResultSet, PageElement

from fulbito.models.data import CopaLigaData, LigaArgData, EuropeanLeagueData
from fulbito.models.top import TopScorers, TopAssists
from fulbito.models.position import TeamPosition, TeamPositionAverage


class PromiedosScrapper:
    URL_COPA_LIGA_ARG = "https://www.promiedos.com.ar/copadeliga"
    URL_LIGA_ARG = "https://www.promiedos.com.ar/primera"
    URL_PREMIER = "https://www.promiedos.com.ar/inglaterra"
    URL_LA_LIGA = "https://www.promiedos.com.ar/espana"
    URL_BUNDESLIGA = "https://www.promiedos.com.ar/alemania"
    URL_SERIEA = "https://www.promiedos.com.ar/italia"

    def get_copa_liga_data(self) -> CopaLigaData:
        response = requests.get(self.URL_COPA_LIGA_ARG).text
        soup = BeautifulSoup(response, "html.parser")
        standings = soup.find_all("table", id="posiciones")
        average_standings = soup.find("table", id="promedios")
        top_tables = soup.find_all("table", id="goleadorest")
        group_a = self._get_standings(TeamPosition, standings[0])
        group_b = self._get_standings(TeamPosition, standings[1])
        annual = self._get_standings(TeamPosition, standings[2])
        average = self._get_standings(TeamPositionAverage, average_standings)
        top_scorers = self._get_top_table(TopScorers, top_tables[0])
        top_assists = self._get_top_table(TopAssists, top_tables[1])
        return CopaLigaData(group_a, group_b, annual, top_scorers, top_assists, average)

    def get_liga_arg_data(self) -> LigaArgData:
        response = requests.get(self.URL_LIGA_ARG).text
        soup = BeautifulSoup(response, "html.parser")
        standings_html = soup.find_all("table", id="posiciones")
        average_standings = soup.find("table", id="promedios")
        top_tables = soup.find_all("table", id="goleadorest")
        standings = self._get_standings(TeamPosition, standings_html[0])
        annual = self._get_standings(TeamPosition, standings_html[1])
        average = self._get_standings(TeamPositionAverage, average_standings)
        top_scorers = self._get_top_table(TopScorers, top_tables[0])
        top_assists = self._get_top_table(TopAssists, top_tables[1])
        return LigaArgData(standings, annual, average, top_scorers, top_assists)

    def get_premier_league_data(self) -> EuropeanLeagueData:
        return self._get_european_league_data(self.URL_PREMIER)

    def get_la_liga_data(self) -> EuropeanLeagueData:
        return self._get_european_league_data(self.URL_LA_LIGA)

    def get_bundesliga_data(self) -> EuropeanLeagueData:
        return self._get_european_league_data(self.URL_BUNDESLIGA)

    def get_serie_a_data(self) -> EuropeanLeagueData:
        return self._get_european_league_data(self.URL_SERIEA)

    def _get_european_league_data(self, url: str) -> EuropeanLeagueData:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        standings_html = soup.find("table", id="posiciones")
        top_tables = soup.find_all("table", id="goleadorest")
        standings = self._get_standings(TeamPosition, standings_html)
        top_scorers = self._get_top_table(TopScorers, top_tables[0])
        top_assists = [] if len(top_tables) < 2 else self._get_top_table(TopAssists, top_tables[1])
        return EuropeanLeagueData(standings, top_scorers, top_assists)

    @staticmethod
    def _get_standings(
            standings_type: Type[TeamPosition | TeamPositionAverage],
            standings: PageElement
    ) -> List[TeamPosition | TeamPositionAverage]:
        positions: List[standings_type] = []
        for position in standings.find("tbody").find_all("tr"):
            team_data: List[str] = []
            for info in position.find_all("td"):
                team_data.append(info.text)
            team = standings_type(team_data)
            positions.append(team)
        return positions

    @staticmethod
    def _get_top_table(top_type: Type[TopScorers | TopAssists], table: ResultSet) -> List[TopScorers | TopAssists]:
        scorers: List[top_type] = []
        position: int = 1
        for scorer_row in table.find_all("tr", {"class": ["punt", "pr", "ipr"]}):
            scorer_info: List[str] = []
            for info in scorer_row.find_all("td"):
                scorer_info.append(info.find(text=True))
            scorers.append(top_type(scorer_info, position))
            position += 1
        return scorers
