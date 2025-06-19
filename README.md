
# Backend Unificado de Apuestas de Valor

Este backend combina scraping real o simulado desde Forebet, SoccerVista y TotalCorner.

- `/apuestas` → JSON con predicciones, coincidencias y valor esperado

Deploy en Render:
- Usa `uvicorn main:app --host 0.0.0.0 --port 10000`
