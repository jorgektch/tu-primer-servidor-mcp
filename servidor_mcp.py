"""Primer servidor MCP, SDK oficial v2 (Python 3.11+).

stdio: python servidor_mcp.py
Inspector: mcp dev servidor_mcp.py
HTTP (solo local): mcp run servidor_mcp.py --transport streamable-http

Nunca imprimas en stdout al iniciar un servidor stdio: lleva el protocolo.
"""
from __future__ import annotations
import json
from mcp.server import MCPServer
import catalogo

mcp = MCPServer(
    'Tienda-Educativa-MCP',
    instructions='Catálogo ficticio: solo consultas de lectura y cotizaciones. No realizar compras ni pagos.'
)

@mcp.tool()
def consultar_stock(producto: str) -> dict:
    """Consulta el stock de un producto ficticio; no modifica inventario."""
    return catalogo.consultar_stock(producto)

@mcp.tool()
def consultar_precio(producto: str) -> dict:
    """Consulta el precio en PEN de un producto del catálogo simulado."""
    return catalogo.consultar_precio(producto)

@mcp.tool()
def cotizar_producto(producto: str, cantidad: int) -> dict:
    """Cotiza unidades disponibles sin pagos, ventas ni efectos secundarios."""
    return catalogo.cotizar_producto(producto,cantidad)

@mcp.resource('inventario://catalogo')
def recurso_catalogo() -> str:
    """Catálogo público ficticio completo, solo lectura."""
    return json.dumps(catalogo.inventario(),ensure_ascii=False)

@mcp.resource('inventario://producto/{producto}')
def recurso_producto(producto: str) -> str:
    """Datos de un producto; las URI no permiten rutas de archivos arbitrarias."""
    p=catalogo.producto_por_nombre(producto)
    return json.dumps(p if p is not None else {'error':'Producto no encontrado'},ensure_ascii=False)

@mcp.prompt()
def guion_cotizacion(producto: str, cantidad: str) -> str:
    """Plantilla educativa de consulta; no constituye una venta."""
    return (
        'Eres un asistente de una tienda completamente ficticia. '
        f'Consulta el stock y cotiza {cantidad} unidad(es) de {producto}. '
        'Usa exclusivamente las herramientas del servidor para cifras y stock. '
        'No solicites datos personales ni pagos. Indica que es una simulación.'
    )

if __name__ == '__main__':
    mcp.run()  # stdio por defecto. El host gestiona el proceso.
