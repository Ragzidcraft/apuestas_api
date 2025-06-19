
from fastapi import FastAPI
from scrapers.demo_data import obtener_demo_eventos
from scrapers.forebet import scrap_forebet_prediccion
from scrapers.soccervista import scrap_soccervista_prob
from scrapers.totalcorner import scrap_totalcorner_dummy
from utils.valor import calcular_valor, calcular_coincidencias

app = FastAPI()

@app.get("/")
def root():
    return {"message": "✅ Backend unificado activo con múltiples scrapers"}

@app.get("/apuestas")
def apuestas():
    eventos = obtener_demo_eventos()
    resultados = []

    for e in eventos:
        pred_forebet = scrap_forebet_prediccion(e["evento"])
        pred_sv = scrap_soccervista_prob(e["evento"])
        pred_tc = scrap_totalcorner_dummy(e["evento"])
        tipo, coincidencias, promedio = calcular_coincidencias(e["probabilidades"])
        valor = calcular_valor(promedio, e["cuota"])
        resultados.append({
            "Evento": e["evento"],
            "Mercado": e["mercado"],
            "Selección": e["seleccion"],
            "Cuota": e["cuota"],
            "Promedio de probabilidad": promedio,
            "Coincidencias": tipo,
            "Valor esperado": valor,
            "Pred. Forebet": pred_forebet,
            "Pred. SoccerVista": pred_sv,
            "Pred. TotalCorner": pred_tc
        })
    return {"apuestas": resultados}
