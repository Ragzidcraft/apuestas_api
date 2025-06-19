
# Backend Apuestas con Scraping Real de SoccerVista

Este backend consulta predicciones reales desde SoccerVista para emparejar con datos simulados de eventos y mostrar apuestas de valor.

- `/` → Estado del servicio
- `/apuestas` → JSON con resultados + predicción de SoccerVista

Despliegue en Render:
- Python
- Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
