
from fastapi import FastAPI
from scrapers.demo_data import obtener_demo_eventos
from utils.valor import calcular_valor, calcular_coincidencias

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Demo Apuestas de Valor corriendo"}

@app.get("/apuestas")
def apuestas():
    eventos = obtener_demo_eventos()
    resultados = []

    for e in eventos:
        tipo, cantidad, promedio = calcular_coincidencias(e["probabilidades"])
        valor = calcular_valor(promedio, e["cuota"])
        resultados.append({
            "Evento": e["evento"],
            "Mercado": e["mercado"],
            "Selección": e["seleccion"],
            "Cuota": e["cuota"],
            "Promedio de probabilidad": promedio,
            "Coincidencias": tipo,
            "Valor esperado": valor
        })
    return {"apuestas": resultados}
