# Evaluación y pruebas

Se emplean tres niveles:

1. **Dominio offline:** `python -m unittest discover -s tests -p 'test_mcp_catalogo.py' -v` sin dependencias externas.
2. **Protocolo real:** `pip install -r requirements.txt` y `python -m unittest discover -s tests -p 'test_mcp_protocol.py' -v`: crea un cliente MCP en memoria y otro por stdio.
3. **Navegador:** `npm install` y `npm run test:e2e`: valida Reveal.js y el visualizador didáctico.

Tabla de regresión:

| Caso | Esperado |
|---|---|
| 2 bicicletas | `total_centimos=170000` y `venta_realizada=false` |
| Consultar casco | `stock=0` |
| Cotizar casco | `STOCK_INSUFICIENTE` |
| Producto inexistente | `PRODUCTO_NO_ENCONTRADO` |
| Cantidad `0`, `true` o `101` | `CANTIDAD_INVALIDA` |
| Herramientas listadas | 3: stock, precio, cotización |
| Resources | catálogo y plantilla de producto |
| Prompts | `guion_cotizacion` |

**Interpretación:** los códigos de dominio viajan como resultados ordinarios `ok:false`; no son necesariamente `is_error=true`. Las herramientas propias no ejecutan acciones externas. Las respuestas del navegador son simuladas y no sustituyen las pruebas del protocolo.
