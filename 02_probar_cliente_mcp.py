"""Paso 2: prueba cliente-servidor MCP verdadero a través de stdio."""
import asyncio
from cliente_mcp import ejecutar

if __name__=='__main__':
    asyncio.run(ejecutar())
