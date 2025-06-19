
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

def normalizar(texto):
    return unidecode(texto.strip().lower().replace("fc", "").replace("cf", "").replace(".", "").replace("-", " ").replace("  ", " "))

def scrap_soccervista_prob(evento):
    url = "https://www.soccervista.com/next_matches.php"
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
        tabla = soup.find("table", {"class": "t1"})
        if not tabla:
            return "No se encontró tabla"

        filas = tabla.find_all("tr")
        home_normal, away_normal = [normalizar(e) for e in evento.split(" vs ")]

        for fila in filas:
            cols = fila.find_all("td")
            if len(cols) >= 6:
                texto_partido = cols[0].get_text(separator=" ").strip()
                pred = cols[5].get_text().strip()
                if " - " in texto_partido:
                    casa, visita = [normalizar(x) for x in texto_partido.split(" - ")]
                    if home_normal in casa and away_normal in visita:
                        return pred
        return "No encontrado"
    except Exception as e:
        return f"Error: {str(e)}"
