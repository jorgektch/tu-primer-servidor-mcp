# Retos de Tu Primer Servidor MCP

## Reto 1 — Nueva Tool: `obtener_categoria`

Implementa una función pura en `catalogo.py` y luego publícala en `servidor_mcp.py` usando `@mcp.tool()`. Prueba `bicicleta`, `casco` y `patineta`. Comprueba que aparezca en `list_tools()` y no introduzcas escrituras.

## Reto 2 — Resource: políticas públicas

Publica `inventario://politicas` con una breve explicación de que la tienda es ficticia y no procesa pagos. Consume la URI con `Client.read_resource()`. No coloques claves ni información privada en el recurso.

## Reto 3 — Prompt personalizado

Crea `guion_consulta_stock(producto: str)`. Comprueba en Inspector y con `Client.get_prompt()` que el argumento se incorpora correctamente al mensaje. Recuerda que un Prompt no ejecuta la tool por sí solo.

## Reto 4 — Compatibilidad de transportes

Ejecuta el mismo cliente contra stdio y contra Streamable HTTP **solo local**. Compara los nombres y esquemas de Tools. ¿Qué cambia en la conexión y qué no cambia en el servidor?

## Reto 5 — Seguridad y fiabilidad

Testea argumentos inválidos, producto desconocido, solicitudes de compra/pago y una entrada que parezca una ruta de archivo. Explica por qué una descripción de tool no reemplaza las validaciones. No expongas un endpoint público para esta actividad.

## Reto 6 — Conexión con el taller de agentes (avanzado)

Dibuja el diagrama host → cliente MCP → servidor. Discute quién decide una llamada y dónde verificar permisos. La integración con un LLM es opcional, y no requiere reescribir el servidor educativo.

**Ver soluciones:** [`soluciones.py`](soluciones.py) (orientativas, no sustituyen el trabajo del estudiante).
