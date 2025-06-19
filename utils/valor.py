
def calcular_valor(prob, cuota):
    return round((prob * cuota) - 1, 3)

def calcular_coincidencias(prob_dict):
    if not prob_dict:
        return "No hay datos", 0, None
    valores = list(prob_dict.values())
    promedio = round(sum(valores) / len(valores), 3)
    coincidencias = sum(1 for p in valores if abs(p - promedio) <= 0.15)
    tipo = {2: "Doble", 3: "Triple", 4: "Cuádruple", 5: "Quíntuple"}.get(coincidencias, f"{coincidencias} coincidencias")
    return tipo, coincidencias, promedio
