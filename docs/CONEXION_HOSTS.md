# Conectar nuestro servidor MCP a un host real

Nuestro proyecto ya incluye un **cliente real sin modelo** (`cliente_mcp.py`). Si deseas consumir las herramientas desde una aplicación con LLM, necesitas conectar un **host compatible** con la revisión del protocolo admitida por su cliente.

## Antes de configurar un host

```bash
python -m pip install -r requirements.txt
python 02_probar_cliente_mcp.py
mcp dev servidor_mcp.py
```

Comprueba que el servidor enumera `consultar_stock`, `consultar_precio` y `cotizar_producto`, el recurso y el prompt. Si no funciona aquí, tampoco funcionará en un host externo.

## Claude Desktop (ejemplo local)

El SDK oficial puede registrar el servidor en Claude Desktop:

```bash
mcp install servidor_mcp.py
```

El host ejecutará un subproceso stdio local. Es posible que necesites instalar y abrir Claude Desktop una vez antes de usar ese comando. Reinicia la aplicación después del registro. Revisa los permisos ofrecidos a las herramientas.

## Cursor (configuración ilustrativa)

Guarda el siguiente JSON en `.cursor/mcp.json` de tu proyecto, sustituyendo la **ruta absoluta** y utilizando `uv` disponible en el PATH del host:

```json
{
  "mcpServers": {
    "tienda-educativa": {
      "command": "uv",
      "args": ["run", "--with", "mcp[cli]>=2,<3", "mcp", "run", "/RUTA/ABSOLUTA/servidor_mcp.py"]
    }
  }
}
```

## VS Code (configuración ilustrativa)

En `.vscode/mcp.json`, la clave es `servers` y se incluye `type`:

```json
{
  "servers": {
    "tienda-educativa": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "--with", "mcp[cli]>=2,<3", "mcp", "run", "/RUTA/ABSOLUTA/servidor_mcp.py"]
    }
  }
}
```

Estas configuraciones son **ejemplos**, no se activan automáticamente. Las interfaces y requisitos del host pueden cambiar, y algunos clientes todavía pueden utilizar revisiones anteriores del protocolo. Verifica la versión del host y sus permisos antes de su uso.

## Seguridad

- El servidor de este taller **no exige autenticación** porque su inventario es ficticio y el uso es local; no lo expongas a Internet sin un diseño de seguridad específico.
- El host debe requerir la autorización adecuada para invocar herramientas. No basta con poner una descripción que diga “solo consulta”.
- Nunca coloques claves en las configuraciones compartidas o archivos versionados.
- Evita ejecutar servidores MCP de terceros sin revisar su código y permisos.

**Fuente:** [MCP Python SDK — Connect to a real host](https://py.sdk.modelcontextprotocol.io/get-started/real-host/).
