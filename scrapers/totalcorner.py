
def scrap_totalcorner_dummy(evento):
    if "Real Madrid" in evento:
        return "Alta cantidad de córners"
    elif "Man City" in evento:
        return "Pocas tarjetas"
    elif "Juventus" in evento:
        return "Primer gol temprano"
    return "No hay datos"
