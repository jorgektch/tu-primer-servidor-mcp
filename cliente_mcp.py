"""Cliente MCP REAL (sin LLM): stdio o HTTP, descubre e invoca capacidades."""
from __future__ import annotations
import argparse
import asyncio
import json
import sys
from pathlib import Path
from mcp import Client, StdioServerParameters
from mcp.types import TextResourceContents

async def ejecutar(http: str | None = None) -> None:
    origen = http or StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).resolve().with_name('servidor_mcp.py'))],
    )
    async with Client(origen) as cliente:
        tools = await cliente.list_tools()
        print('HERRAMIENTAS:', [t.name for t in tools.tools])
        recursos = await cliente.list_resources()
        print('RECURSOS:', [str(r.uri) for r in recursos.resources])
        plantillas = await cliente.list_resource_templates()
        print('PLANTILLAS:', [r.uri_template for r in plantillas.resource_templates])
        prompts = await cliente.list_prompts()
        print('PROMPTS:', [p.name for p in prompts.prompts])

        result = await cliente.call_tool('cotizar_producto',{'producto':'bicicletas','cantidad':2})
        if result.is_error:
            raise RuntimeError('Error MCP en la cotización')
        print('COTIZACIÓN:', json.dumps(result.structured_content,ensure_ascii=False))

        doc = await cliente.read_resource('inventario://catalogo')
        for block in doc.contents:
            if isinstance(block,TextResourceContents):
                print('RECURSO:',block.text[:180]+'...')

        prompt = await cliente.get_prompt('guion_cotizacion',{'producto':'bicicleta','cantidad':'2'})
        print('PROMPT:',len(prompt.messages),'mensaje(s)')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Cliente de prueba MCP sin LLM ni claves')
    parser.add_argument('--http',help='Endpoint Streamable HTTP, ej.: http://127.0.0.1:8000/mcp')
    args=parser.parse_args()
    asyncio.run(ejecutar(args.http))
