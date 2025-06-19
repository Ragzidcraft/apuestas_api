
# Backend de Apuestas de Valor Inteligente (Demo Extendida)

Este proyecto simula un backend con scraping de plataformas externas (SoccerVista, Forebet, TotalCorner) y muestra valor esperado, coincidencias y selección recomendada.

## Endpoints

- `/` → Estado del servicio
- `/apuestas` → JSON con eventos de valor

## Despliegue

1. Sube esto a GitHub
2. Conéctalo a https://render.com como Web Service
3. Usa el Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
