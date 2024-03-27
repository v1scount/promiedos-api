from fastapi import FastAPI, HTTPException
from requests import RequestException
from starlette.responses import HTMLResponse

from fulbito.scraper.promiedos import PromiedosScraper


app = FastAPI()
scraper = PromiedosScraper()


@app.get("/", response_class=HTMLResponse)
def fulbito():
    return """
    <html>
        <head>
            <title>Fulbito!</title>
        </head>
        <body>
            <h1>Fulbito</h1>
            <p>Fulbito is a Football API. The data is extracted from <a href="https://promiedos.com.ar">Promiedos<a/> via web scrapping.</p>
            <p>This API supports the following tournaments:</p>
            <ul>
                <li><a href="/copa-de-la-liga">Copa de la Liga Argentina</a></li>
                <li><a href="/liga-argentina">Liga Argentina</a></li>
                <li><a href="/premier-league">Premier League</a></li>
                <li><a href="/la-liga">La Liga</a></li>
                <li><a href="/bundesliga">Bundesliga</a></li>
                <li><a href="/serie-a">Serie A</a></li>
            </ul>
        </body>
    </html>
    """


@app.get("/copa-de-la-liga")
def copa_liga_arg():
    try:
        return scraper.get_copa_liga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_COPA_LIGA_ARG}.")


@app.get("/liga-argentina")
def liga_arg():
    try:
        return scraper.get_liga_arg_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_LIGA_ARG}.")


@app.get("/premier-league")
def premier_league():
    try:
        return scraper.get_premier_league_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_PREMIER}.")


@app.get("/la-liga")
def la_liga():
    try:
        return scraper.get_la_liga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_LA_LIGA}.")


@app.get("/bundesliga")
def bundesliga():
    try:
        return scraper.get_bundesliga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_BUNDESLIGA}.")


@app.get("/serie-a")
def serie_a():
    try:
        return scraper.get_serie_a_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scraper.URL_SERIEA}.")
