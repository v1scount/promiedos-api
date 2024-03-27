from fastapi import FastAPI, HTTPException
from requests import RequestException
from starlette.responses import HTMLResponse

from fulbito.scrapper.promiedos import PromiedosScrapper


app = FastAPI()
scrapper = PromiedosScrapper()


@app.get("/", response_class=HTMLResponse)
def fulbito():
    return """
    <html>
        <head>
            <title>Fulbito!</title>
        </head>
        <body>
            <h1>Fulbito</h1>
            <p>Fulbito is a Football API. The data is extracted from https://promiedos.com.ar via web scrapping.</p>
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
        return scrapper.get_copa_liga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_COPA_LIGA_ARG}.")


@app.get("/liga-argentina")
def liga_arg():
    try:
        return scrapper.get_liga_arg_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_LIGA_ARG}.")


@app.get("/premier-league")
def premier_league():
    try:
        return scrapper.get_premier_league_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_PREMIER}.")


@app.get("/la-liga")
def la_liga():
    try:
        return scrapper.get_la_liga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_LA_LIGA}.")


@app.get("/bundesliga")
def bundesliga():
    try:
        return scrapper.get_bundesliga_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_BUNDESLIGA}.")


@app.get("/serie-a")
def serie_a():
    try:
        return scrapper.get_serie_a_data()
    except RequestException:
        raise HTTPException(status_code=500, detail=f"Couldn't get info from {scrapper.URL_SERIEA}.")
