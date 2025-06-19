
def scrap_forebet_prediccion(evento):
    try:
        # Aquí iría el scraping real
        if "Real Madrid" in evento:
            return "1 | 2-1 | Over | BTTS: Yes"
        elif "Man City" in evento:
            return "X | 1-1 | Under | BTTS: No"
        elif "Juventus" in evento:
            return "2 | 1-2 | Over | BTTS: Yes"
        else:
            return "No encontrado"
    except Exception as e:
        return f"Error: {str(e)}"
