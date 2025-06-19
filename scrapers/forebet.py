import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

def normalizar(texto):
    return unidecode(texto.strip().lower().replace("fc", "").replace("cf", "").replace(".", "").replace("-", " ").replace("  ", " "))

def scrap_forebet_prediccion(evento):
    url = "https://www.forebet.com/en/football-predictions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            return "Error acceso"

        soup = BeautifulSoup(res.text, "html.parser")
        tabla = soup.find("table", {"class": "schema"})
        if not tabla:
            return "No se encontró tabla"

        filas = tabla.find_all("tr", recursive=False)
        home_n, away_n = [normalizar(e) for e in evento.split(" vs ")]

        for fila in filas:
            cols = fila.find_all("td", recursive=False)
            if len(cols) < 7:
                continue
            equipos = cols[1].get_text(separator=" vs ").strip()
            if " - " not in equipos:
                continue
            casa, visita = [normalizar(e) for e in equipos.split(" - ")]
            if home_n in casa and away_n in visita:
                pred_1x2 = cols[3].text.strip()
                score = cols[2].text.strip()
                ou = cols[5].text.strip()
                btts = cols[6].text.strip()
                return f"{pred_1x2} | {score} | {ou} | BTTS: {btts}"
        return "No encontrado"
    except Exception as e:
        return f"Error: {str(e)}"