# Fundamentos de Model Context Protocol (MCP)

## Qué resuelve
MCP establece un contrato de interoperabilidad entre una aplicación **host** (y sus clientes MCP) y un **servidor** que expone capacidades. En un host con LLM, el modelo puede solicitar invocar una herramienta, pero el host/client sigue siendo responsable de los permisos y de la ejecución; MCP no autoriza nada por sí solo.

```mermaid
flowchart LR
  U[Usuario] --> H[Host de IA]
  H --> C[Cliente MCP]
  C <-->|MCP| S[Servidor MCP]
  S --> B[Servicios y datos]
```

## Los tres mecanismos

| Primitiva | Operación principal | Nuestro ejemplo | Observación |
|---|---|---|---|
| Tool | `tools/list`, `tools/call` | `cotizar_producto` | Puede tener efectos secundarios, aunque este servidor no tiene ninguno |
| Resource | `resources/list`, `resources/read` | `inventario://catalogo` | Contexto identificado por URI; solo lectura en el ejemplo |
| Prompt | `prompts/list`, `prompts/get` | `guion_cotizacion` | Mensajes reutilizables, no un LLM ni una función de negocio |

Además hay **plantillas de URI** como `inventario://producto/{producto}`, enumerables mediante `resources/templates/list`.

## stdio vs Streamable HTTP

- **stdio:** transporte local sobre `stdin` y `stdout`. El host lanza un proceso. La salida estándar no debe contener mensajes de depuración antes de que arranque el transporte.
- **Streamable HTTP:** transporte sobre HTTP, adecuado para servicios. Un despliegue público debe incorporar autenticación y autorización de acuerdo al modelo de amenazas.
- **SSE independiente:** transporte heredado, no recomendado para nuevos desarrollos.

## Qué cambió en el SDK oficial v2

El SDK oficial pasó de `FastMCP` a `MCPServer`. Este proyecto usa `from mcp.server import MCPServer` y el nuevo `from mcp import Client`. Para no mezclar tutoriales de distintas versiones fijamos `mcp[cli]>=2.0,<3` y Python 3.11+. La versión del protocolo y su compatibilidad se acuerdan entre cliente y servidor; no asumas que todos los hosts admiten las mismas revisiones.

## ¿Esto es un agente?

No. Nuestro cliente MCP funciona sin LLM. Un **agente** del taller anterior puede conectar con herramientas mediante un runtime especializado. Si el host implementa un cliente MCP, puede descubrir capacidades sin copiar directamente las funciones Python.

## Fuentes

- https://modelcontextprotocol.io/
- https://py.sdk.modelcontextprotocol.io/get-started/first-steps/
- https://py.sdk.modelcontextprotocol.io/client/
- https://py.sdk.modelcontextprotocol.io/migration/
