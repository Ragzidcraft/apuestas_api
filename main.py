from fastapi import FastAPI
from scrapers.demo_data import obtener_demo_eventos
from scrapers.forebet import scrap_forebet_prediccion
from utils.valor import calcular_valor, calcular_coincidencias

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Servicio de Apuestas con Forebet"}

@app.get("/apuestas")
def apuestas():
    eventos = obtener_demo_eventos()
    resultados = []

    for e in eventos:
        pred_forebet = scrap_forebet_prediccion(e["evento"])
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
            "Pred. Forebet": pred_forebet
        })
    return {"apuestas": resultados}