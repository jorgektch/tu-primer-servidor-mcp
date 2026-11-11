# Uso del explorador visual

Abre `demo/index.html` desde un servidor HTTP que sirva la raíz del proyecto:

```bash
python -m http.server 8765
```

Entra a `http://127.0.0.1:8765/demo/`. Escoge escenarios para ver **solicitudes JSON-RPC ilustrativas** y **respuestas simuladas**:

- `tools/list`: tres herramientas.
- `tools/call`: cotización correcta y errores de dominio.
- `resources/read`: catálogo de prueba.
- `prompts/get`: plantilla de atención.

La demo lee el mismo `data/inventario.json` que usa Python, pero **no inicia un servidor MCP, no hace una conexión MCP y no utiliza un modelo de IA**. Su finalidad es enseñar visualmente el intercambio.

Para comprobar una interacción MCP real, usa `pip install -r requirements.txt` y `python 02_probar_cliente_mcp.py`. Para inspección visual real de las primitivas, usa `mcp dev servidor_mcp.py` con el SDK v2 e Inspector disponibles.
