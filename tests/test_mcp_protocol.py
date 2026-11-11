"""Integración real del SDK v2: Client con servidor en memoria y stdio.

GitHub Actions instala mcp[cli]>=2,<3. Si no está instalado, se omiten
estas pruebas localmente; los tests de dominio offline siguen ejecutándose.
"""
import asyncio
import importlib.util
import sys
import unittest
from pathlib import Path

HAS_MCP=importlib.util.find_spec('mcp') is not None

@unittest.skipUnless(HAS_MCP,'Instala mcp[cli]>=2,<3 para pruebas de protocolo')
class MCPProtocolTests(unittest.TestCase):
    def test_real_mcp_inprocess(self):
        from mcp import Client
        from servidor_mcp import mcp
        async def run():
            async with Client(mcp,raise_exceptions=True) as c:
                result=await c.list_tools()
                self.assertEqual({t.name for t in result.tools},
                    {'consultar_stock','consultar_precio','cotizar_producto'})
                cot=await c.call_tool('cotizar_producto',{'producto':'bicicleta','cantidad':2})
                self.assertFalse(cot.is_error)
                d=cot.structured_content
                if isinstance(d,dict) and 'result' in d and isinstance(d['result'],dict):d=d['result']
                self.assertEqual(d['total_centimos'],170000)
                self.assertFalse(d['venta_realizada'])
                resources=await c.list_resources()
                self.assertIn('inventario://catalogo',{str(x.uri) for x in resources.resources})
                resource=await c.read_resource('inventario://catalogo')
                self.assertTrue(any('bicicleta' in getattr(block,'text','') for block in resource.contents))
                templates=await c.list_resource_templates()
                self.assertTrue(any('producto/{producto}' in x.uri_template for x in templates.resource_templates))
                prompts=await c.list_prompts()
                self.assertIn('guion_cotizacion',{p.name for p in prompts.prompts})
                prompt=await c.get_prompt('guion_cotizacion',{'producto':'bicicleta','cantidad':'2'})
                self.assertTrue(prompt.messages)
        asyncio.run(run())
    def test_actual_stdio_transport(self):
        from mcp import Client,StdioServerParameters
        async def run():
            params=StdioServerParameters(command=sys.executable,
                args=[str(Path(__file__).resolve().parents[1]/'servidor_mcp.py')])
            async with Client(params) as c:
                tools=await c.list_tools()
                self.assertEqual(len(tools.tools),3)
                result=await c.call_tool('consultar_stock',{'producto':'casco'})
                self.assertFalse(result.is_error)
                data=result.structured_content
                if 'result' in data and isinstance(data['result'],dict):data=data['result']
                self.assertEqual(data['stock'],0)
        asyncio.run(run())
if __name__=='__main__':unittest.main()
