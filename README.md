# Backend con Scraping Real desde Forebet

Este backend consulta predicciones reales desde Forebet (1X2, Over/Under, BTTS, marcador estimado).

- `/` → Estado del servicio
- `/apuestas` → JSON con resultados + predicción de Forebet

## Despliegue en Render

Start Command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```