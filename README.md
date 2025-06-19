# Backend con Scraping Real desde SoccerVista (next_matches.php)

Este backend consulta predicciones reales desde una URL alternativa de SoccerVista (`next_matches.php`).

- `/` → Estado del servicio
- `/apuestas` → JSON con predicción 1X2 incluida

## Despliegue en Render

Start Command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```