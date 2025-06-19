
def scrap_soccervista_prob(evento):
    # Este es un mock para simular la predicción de SoccerVista
    if "Real Madrid" in evento:
        return "1"
    elif "Man City" in evento:
        return "Sí"
    elif "Juventus" in evento:
        return "Over"
    return "No hay datos"
