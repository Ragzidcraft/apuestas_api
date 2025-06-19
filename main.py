
from fastapi import FastAPI
from scrapers.demo_data import obtener_demo_eventos
from scrapers.soccervista import scrap_soccervista_prob
from utils.valor import calcular_valor, calcular_coincidencias

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Servicio de Apuestas Inteligente Activo"}

@app.get("/apuestas")
def apuestas():
    eventos = obtener_demo_eventos()
    resultados = []

    for e in eventos:
        pred_sv = scrap_soccervista_prob(e["evento"])
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
            "Pred. SoccerVista": pred_sv
        })
    return {"apuestas": resultados}
