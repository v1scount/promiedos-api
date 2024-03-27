# Fulbito
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Fulbito is a Football API. The data is extracted from [Promiedos](https://promiedos.com.ar) via web scrapping.

This API supports the following tournaments:
- [Copa de la Liga Argentina](https://fulbito-mozb.onrender.com/copa-de-la-liga)
- [Liga Argentina](https://fulbito-mozb.onrender.com/liga-argentina)
- [Premier League](https://fulbito-mozb.onrender.com/premier-league)
- [La Liga](https://fulbito-mozb.onrender.com/premier-league)
- [Bundesliga](https://fulbito-mozb.onrender.com/premier-league)
- [Serie A](https://fulbito-mozb.onrender.com/premier-league)

## Content per tournament
### Copa de Liga Argentina
- Standings groups A & B (points, wins, losses, draws, goals for, goals against, goal diff.).
- Annual standings.
- Average standings.
- Top scorers.
- Top assists.

### Liga Argentina
- Standings (points, wins, losses, draws, goals for, goals against, goal diff.).
- Annual standings.
- Average standings.
- Top scorers.
- Top assists.

### Premier League - La Liga - Serie A 
- Standings (points, wins, losses, draws, goals for, goals against, goal diff.).
- Top scorers.
- Top assists.

### Bundesliga
- Standings (points, wins, losses, draws, goals for, goals against, goal diff.).
- Top scorers.

## How to use it
You can try it [here](https://fulbito-mozb.onrender.com/). Patience, it takes long to load. (Free tier host 😅) 

If you want to run it locally:

Clone the repo and `cd` into it.
```sh
git clone https://github.com/claaj/fulbito.git && cd fulbito
```

Create a virtual enviroment and activate it.
```sh
virtualenv venv && source venv/bin/activate
```

Install deps.
```sh
pip install -r requirements.txt
```

Run it.
```sh
uvicorn fulbito.api:app --reload
```

Open `http://127.0.0.1:8000` in browser, you should see fulbito's landing screen.

## Libraries
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scrapping.
- [Fast Api](https://fastapi.tiangolo.com/) for the API.
- [Pydantic](https://pydantic.dev/) for data validation.
